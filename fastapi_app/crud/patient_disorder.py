from sqlalchemy.orm import Session
from fastapi_app.models import PatientDisorder
from fastapi_app.schemas.patient_disorder import PatientDisorderCreate


def get_all(db: Session):
    return db.query(PatientDisorder).all()

def get_by_ids(db: Session, patient_id: int, disorder_id: int):
    return db.query(PatientDisorder).filter_by(
        patient_id=patient_id, disorder_id=disorder_id
    ).first()

def create(db: Session, obj_in: PatientDisorderCreate):
    db_obj = PatientDisorder(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete(db: Session, patient_id: int, disorder_id: int):
    obj = get_by_ids(db, patient_id, disorder_id)
    if obj:
        db.delete(obj)
        db.commit()
    return obj

