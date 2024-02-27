from pydantic import BaseModel, Field, field_validator
from enum import Enum
from typing import Any, Optional, Sequence

class HplcColumn(Enum):
    shodex_kw_403 = "Showdex KW-403"
    shodex_kw_402_5 =  "Showdex KW-402.5"
    shodex_kw_404 =  "Showdex KW-404"
    shodex_kw_405 =  "Showdex KW-405"
    superdex_200_increase = "Superdex 200 Increase 3.2"
    superdex_6_increase_3_2="Superose 6 Increase 3.2"

class StorageTemperatureOptions(Enum):
    room = "room"
    minus_eighty = -80
    minus_four= -4


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
    column: HplcColumn
    notes: str
    buffer: Buffer

class Batch(BaseModel):
    holder_id: str
    sample_position: str
    sample_name: str
    buffer: Buffer
    concentration: float
    volume: float
    molecular_weight: float
    notes: str
    
    @field_validator("volume")
    @classmethod
    def validate_volume(cls,volume: float):
        if volume < 25:
            raise ValueError("volume must be more than 25ul")
        return volume

class User(BaseModel):
    visit_id: str
    holder_id: str
    name: str
    contact_email: str
    contact_phone_number: Optional[str]
    local_contact: str
    storage_temp: StorageTemperatureOptions
    samples: Sequence[HPLC]| Sequence[Batch]