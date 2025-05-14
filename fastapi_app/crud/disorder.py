from sqlalchemy.orm import Session
from fastapi_app import models, schemas


def create_disorder(db: Session, disorder: schemas.DisorderCreate):
    db_disorder = models.Disorder(**disorder.dict())
    db.add(db_disorder)
    db.commit()
    db.refresh(db_disorder)
    return db_disorder

def get_disorders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Disorder).offset(skip).limit(limit).all()

def get_disorder(db: Session, disorder_id: int):
    return db.query(models.Disorder).filter(models.Disorder.id == disorder_id).first()

def update_disorder(db: Session, disorder_id: int, disorder: schemas.DisorderUpdate):
    db_disorder = db.query(models.Disorder).filter(models.Disorder.id == disorder_id).first()
    if not db_disorder:
        return None
    for key, value in disorder.dict(exclude_unset=True).items():
        setattr(db_disorder, key, value)
    db.commit()
    db.refresh(db_disorder)
    return db_disorder

def delete_disorder(db: Session, disorder_id: int):
    db_disorder = db.query(models.Disorder).filter(models.Disorder.id == disorder_id).first()
    if not db_disorder:
        return None
    db.delete(db_disorder)
    db.commit()
    return db_disorder

