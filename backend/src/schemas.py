from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class EntryBase(BaseModel):
    notes: str
    dirty: Optional[bool]


class EntryCreate(EntryBase):
    pass

    class Config:
        schema_extra = {
            "example": {
                "notes": "Baby seemed happy",
                "dirty": False
            }
        }


class Entry(EntryBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
