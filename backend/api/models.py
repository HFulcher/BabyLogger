from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from database import Base


class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), index=True)
    entry_type = Column(String)
    duration = Column(Integer, nullable=True)
    wee = Column(Boolean, nullable=True)
    poo = Column(Boolean, nullable=True)
    full = Column(Boolean, nullable=True)
    notes = Column(String, nullable=True)
