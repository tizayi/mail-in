from pydantic import BaseModel, field_validator, model_validator, EmailStr, Field
import yaml
from typing import TypedDict, Sequence, Optional
from enum import StrEnum, Enum

class AppConfig(TypedDict):
    hplc_column: Sequence[str]
    storage_temp: Sequence[str]

with open("./config.yml") as config_yaml:
    config: AppConfig = yaml.safe_load(config_yaml)

ColumnOptions = StrEnum("ColumnOptions",config["hplc_column"])
StorageTempOptions = StrEnum("StorageTempOptions",config["storage_temp"])


class HolderType(Enum):
    HPLC = "hplc"
    Batch = "batch"


class Buffer(BaseModel):
    id: str
    name: str
    holder_id: str
    ph: Optional[int] = Field(default=None)
    position: Optional[int] = Field(default=None)

    @field_validator("ph")
    @classmethod
    def validate_ph(cls, ph: float) -> float:
        if ph and (ph < 0 or ph > 14):
            raise ValueError('pH must be between 0 and 14')
        return ph

    @field_validator("position")
    @classmethod
    def validate_position(cls, position: int) -> int:
        if position and position(position < 1 or position > 9):
            raise ValueError("position must be between 1 and 9 inclusive")
        return position

class Sample(BaseModel):
    id: str
    holder_id: str
    position: int
    concentration: Optional[float] = Field(default=None)
    volume: Optional[float] = Field(default=None)
    molecular_weight: Optional[float] = Field(default=None)
    column: Optional[ColumnOptions] = Field(default=None)
    buffer_id: str
    notes: str

    @field_validator("position")
    @classmethod
    def validate_position(cls, position: int) -> int:
        if position and position(position < 1 or position > 9):
            raise ValueError("position must be between 1 and 9 inclusive")
        return position

class Holder(BaseModel):
    id: str
    visit_id: str
    type: HolderType
    storage_temp: StorageTempOptions


class Visit(BaseModel):
    id: str
    name: str
    email: EmailStr
    phone_number: Optional[str] = Field(default=None)
    local_contact: str  

    @field_validator("contact_phone_number")
    @classmethod
    def check_phone_number(cls, number: str):
        if not number.isdigit() or len(number) != 10:
            raise ValueError("Inavlid phone number format")
        return number

class SaxMailIn(BaseModel):
    visit: Visit
    holder: Holder
    samples: Sequence[Sample]
    buffers: Sequence[Buffer]

    @model_validator(mode='after')
    def validate_samples_and_buffers(self) -> 'SaxMailIn':
        sample_positions = [sample.position for sample in self.samples]
        buffer_positions = [buffer.position for buffer in self.buffers]
        buffer_ids = [buffer.id for buffer in self.buffers]
        sample_buffers = [sample.buffer_id for sample in self.samples]

        # Check all positions are unique
        if len(sample_positions) + len(buffer_positions) != len(set(buffer_positions).update(sample_positions)):
            raise ValueError(" Sample and buffer position are not unique")
        
        # There must be atleast one buffer
        if len(buffer_positions) < 1:
            raise ValueError("There must be atleast one buffer")
        
       # Check batch mode buffers exist
        if (self.holder.type == HolderType.Batch):
            if set(sample_buffers) != set(buffer_ids):
                raise ValueError("Sample Buffers in Batch mode must coresspond to a real buffer")
            return self
        
        # Check HPLC mode only has one buffer
        if len(buffer_positions) != 1 or buffer_positions[0] != None:
            raise ValueError("In HPLC mode there is only one buffer with no position")

        # check HPLC mode buffers 
        if not all(sample_buffers) == buffer_ids[0]:
            raise ValueError("In HPLC mode samples have the same buffer")
        
        return self
