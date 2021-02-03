from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from database import Base


class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), index=True)
    notes = Column(String)
    dirty = Column(Boolean, default=False)
