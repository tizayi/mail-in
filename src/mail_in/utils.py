from pydantic import BaseModel, Field, field_validator
from typing import Any, Optional, Sequence


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
    column: str
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
    storage_temp: str
    samples: Sequence[HPLC]| Sequence[Batch]