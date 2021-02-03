from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import crud
import models
import schemas
from typing import Optional, List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/entry/{entry_id}/", response_model=schemas.Entry)
def get_entry(entry_id: int, db: Session = Depends(get_db)):
    db_entry = crud.get_entry(entry_id=entry_id, db=db)

    if db_entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")

    return db_entry


@app.get("/entries/", response_model=List[schemas.Entry])
def get_entries(db: Session = Depends(get_db)):
    db_entries = crud.get_all_entries(db=db)

    if len(db_entries) == 0:
        raise HTTPException(status_code=404, detail="There are no entries")

    return db_entries


@app.post("/entry/", response_model=schemas.Entry)
def create_entry(entry: schemas.EntryCreate, db: Session = Depends(get_db)):
    return crud.create_entry(entry=entry, db=db)


@app.delete("/entry/{entry_id}")
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    possible_entry = db.query(models.Entry).filter(
        models.Entry.id == entry_id).first()

    if possible_entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")

    return crud.delete_entry(entry_id=entry_id, db=db)
