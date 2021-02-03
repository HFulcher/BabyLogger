from sqlalchemy.orm import Session
import models
import schemas


def get_entry(entry_id: int, db: Session):
    return db.query(models.Entry).filter(models.Entry.id == entry_id).first()


def get_all_entries(db: Session):
    return db.query(models.Entry).all()


def create_entry(entry: schemas.EntryCreate, db: Session):
    new_entry = models.Entry(notes=entry.notes, dirty=entry.dirty)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry


def delete_entry(entry_id: int, db: Session):
    db.query(models.Entry).filter(models.Entry.id == entry_id).delete()
    db.commit()

    return {"status": "200", "message": "Entry deleted"}
