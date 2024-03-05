from pydantic import BaseModel, field_validator, model_validator, EmailStr, Field
import yaml
from typing import TypedDict, Sequence, Optional
from enum import StrEnum

class AppConfig(TypedDict):
    hplc_column: Sequence[str]
    storage_temp: Sequence[str]

with open("./config.yml") as config_yaml:
    config: AppConfig = yaml.safe_load(config_yaml)

ColumnOptions = StrEnum("ColumnOptions",config["hplc_column"])
StorageTempOptions = StrEnum("StorageTempOptions",config["storage_temp"])

class Buffer(BaseModel):
    id: str
    ph: Optional[float] = Field(default=None)
    position: Optional[int] = Field(default=None)

    @field_validator("ph")
    @classmethod
    def validate_ph(cls, ph: float) -> float:
        if ph < 0 or ph > 14:
            raise ValueError('pg')
        return ph
    
    @field_validator("position")
    @classmethod
    def validate(cls, position: Optional[int]) -> Optional[int]:
        if position and (position < 1 or position > 9):
            raise ValueError("position must be between 1 and 9 inclusive or none")
        return position


class HplcSample(BaseModel):
    name: str
    position: int
    concentration: Optional[float] = Field(default=None)
    volume: Optional[float] = Field(default=None)
    molecular_weight: Optional[float] = Field(default=None)
    column: ColumnOptions
    notes: str

    @field_validator("position")
    @classmethod
    def validate(cls, position: int) -> int:
        if position and (position < 1 or position > 9):
            raise ValueError("position must be between 1 and 9 inclusive or none")
        return position


class HPLCHolder(BaseModel):
    storage_temp: StorageTempOptions
    holder_id: str
    buffer: Buffer
    samples: Sequence[HplcSample]

    @field_validator("buffer")
    @classmethod
    def check_buffer_position_is_none(cls, buffer: Buffer):
        if buffer.position != None:
            raise ValueError("Hplc buffer is not in a holder position")
        return buffer

    @field_validator("samples")
    @classmethod
    def check_sample_position_are_unique(cls, samples: Sequence[HplcSample]) -> Sequence[HplcSample]:
        sample_positions = [sample.position for sample in samples]
        if not (len(sample_positions) == len(set(sample_positions))):
            raise ValueError("sample positions must be unique")
        return samples
    
    @field_validator("samples")
    @classmethod
    def check_sample_names_are_unique(cls, samples: Sequence[HplcSample]) -> Sequence[HplcSample]:
        sample_names = [sample.name for sample in samples]
        if not (len(sample_names) == len(set(sample_names))):
            raise ValueError("sample names must be unique")
        return samples


class BatchSample(BaseModel):
    name: str
    position: int
    concentration: Optional[float] = Field(default=None)
    volume: Optional[float] = Field(default=None)
    molecular_weight: Optional[float] = Field(default=None)
    buffer_position: Optional[int] = Field(default=None)
    notes: str

    @field_validator("position", "buffer_position")
    @classmethod
    def check_sample_position_is_valid(cls, position: int) -> int:
        if position and (position < 1 or position > 9):
            raise ValueError("position must be between 1 and 9 inclusive or none")
        return position


class BatchHolder(BaseModel):
    storage_temp: StorageTempOptions
    holder_id: str
    samples: Sequence[BatchSample]
    buffers: Sequence[Buffer]

    @field_validator("buffers")
    @classmethod
    def check_at_least_one_buffer(cls, buffers: Sequence[Buffer]):
        if len(buffers)<1:
            ValueError("Batch mode must have atleast one buffer")
        return buffers

    @model_validator(mode='after')
    def check_sample_buffer_positions_are_unique(self) -> 'BatchHolder':
        buffer_positions = [buffer.position for buffer in self.buffers]
        sample_positions = [sample.position for sample in self.samples]
        position_set = set(sample_positions)
        position_set.update(buffer_positions)
        if not ( len(sample_positions) + len(buffer_positions) == len(position_set)):
            raise ValueError("sample and buffer positions must all be unique")
        return self
    
    @model_validator(mode='after')
    def check_sample_buffer_names_are_unique(self) -> 'BatchHolder':
        buffer_names = [buffer.id for buffer in self.buffers]
        sample_names = [sample.name for sample in self.samples]
        name_set = set(sample_names)
        name_set.update(buffer_names)
        if not (len(sample_names) + len(buffer_names) == len(name_set)):
            raise ValueError("sample and buffer positions must all be unique")
        return self


class Visit(BaseModel):
    visit_id: str
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
    user: Visit
    batch_holders: Sequence[BatchHolder]
    hplc_holders: Sequence[HPLCHolder]

