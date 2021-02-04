from sqlalchemy.orm import Session
import models
import schemas


def get_all_entries(db: Session):
    return db.query(models.Entry).all()


def get_entries_by_type(entry_type: str, db: Session):
    return db.query(models.Entry).filter(models.Entry.entry_type == entry_type).all()


def get_entry(entry_id: int, db: Session):
    return db.query(models.Entry).filter(models.Entry.id == entry_id).first()


def create_entry(entry: schemas.EntryCreate, db: Session):
    new_entry = models.Entry(
        entry_type=entry.entry_type,
        duration=entry.duration,
        wee=entry.wee,
        poo=entry.poo,
        full=entry.full,
        notes=entry.notes
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry


def delete_entry(entry_id: int, db: Session):
    db.query(models.Entry).filter(models.Entry.id == entry_id).delete()
    db.commit()

    return {"status": "200", "message": "Entry deleted"}


def delete_all_entries(db: Session):
    db.query(models.Entry).delete()
    db.commit()

    return {"status": "200", "message": "All entries deleted"}


def delete_all_entries_by_type(entry_type: str, db: Session):
    db.query(models.Entry).filter(
        models.Entry.entry_type == entry_type).delete()
    db.commit()

    return {"status": "200", "message": "All entries of type {}".format(entry_type)}
