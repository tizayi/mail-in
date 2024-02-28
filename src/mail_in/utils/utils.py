from pydantic import BaseModel, Field, field_validator
from typing import Optional, Sequence
import yaml
from typing import TypedDict, List
from enum import Enum, StrEnum

class AppConfig(TypedDict):
    hplc_column: List[str]
    storage_temp: List[str]

with open("./config.yml") as config_yaml:
    config: AppConfig = yaml.safe_load(config_yaml)

ColumnOptions = StrEnum("ColumnOptions",config["hplc_column"])
StorageTempOptions = StrEnum("StorageTempOptions",config["storage_temp"])

class Buffer(BaseModel):
    identifier: str
    ph: float

    @field_validator("ph")
    @classmethod
    def validate_ph(cls, ph: float) -> float:
        if ph < 0 or ph > 14:
            raise ValueError('pg')
        return ph

class HPLC(BaseModel):
    holder_id: str
    sample_position: str
    sample: str
    flow_rate: float
    concentration: float
    volume: float
    column: ColumnOptions
    notes: str
    buffer: Buffer

    @field_validator("column")
    @classmethod
    def validate_column(cls, column: str):
        if column not in ColumnOptions:
            raise ValueError(f"{column} is not a valid column")
        return column

class Batch(BaseModel):
    holder_id: str
    sample_position: int
    sample_name: str
    buffer: Buffer
    concentration: float
    volume: float
    molecular_weight: float
    notes: str

    @field_validator("sample_position")
    @classmethod
    def validate_simple_position(cls, sample_position: int)-> int:
        if sample_position > 9 or sample_position < 1:
            raise ValueError(f"sample position must be between 1 and 9")
        return sample_position 
    
    @field_validator("volume")
    @classmethod
    def validate_volume(cls, volume: float)-> float:
        if volume < 25:
            raise ValueError("volume must be more than 25ul")
        return volume

class SaxMailIn(BaseModel):
    visit_id: str
    holder_id: str
    name: str
    contact_email: str
    contact_phone_number: Optional[str]
    local_contact: str
    storage_temp: StorageTempOptions
    samples: Sequence[HPLC] | Sequence[Batch]

    @field_validator("storage_temp")
    @classmethod
    def validate_storage_temp(cls, storage_temp: str):
        if storage_temp not in StorageTempOptions:
            raise ValueError(f"{storage_temp} is not a valid storage temperature")
        return storage_temp