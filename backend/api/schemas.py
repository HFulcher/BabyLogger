from pydantic import BaseModel, root_validator
from typing import Optional
from datetime import datetime
from enum import Enum


class TypeEnum(str, Enum):
    feed = 'feed'
    nappy = 'nappy'
    sleep = 'sleep'


class EntryBase(BaseModel):
    entry_type: TypeEnum
    duration: Optional[int] = None
    wee: Optional[bool] = None
    poo: Optional[bool] = None
    full: Optional[bool] = None
    notes: Optional[str] = None

    @root_validator
    def check_feed_type(cls, values):
        et, feed_dur = values.get('entry_type'), values.get('duration')

        if et == "feed" and feed_dur is None:
            raise ValueError("Feed entry must have a duration!")

        return values

    @root_validator
    def check_nappy_type(cls, values):
        et, wee_flag, poo_flag, full_flag = values.get('entry_type'), values.get(
            'wee'), values.get('poo'), values.get('full')

        if et == "nappy" and (wee_flag is None or poo_flag is None or full_flag is None):
            raise ValueError("Nappy entry must have a wee, poo and full flag!")

        return values

    @root_validator
    def check_sleep_type(cls, values):
        et, sleep_dur = values.get('entry_type'), values.get('duration')

        if et == "sleep" and sleep_dur is None:
            raise ValueError("Sleep entry must have a duration!")

        return values

    class Config:
        use_enum_values = True


class EntryCreate(EntryBase):
    pass


class Entry(EntryBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
