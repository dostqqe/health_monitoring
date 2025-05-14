from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_app.crud import patient_disorder as crud
from fastapi_app.schemas.patient_disorder import PatientDisorderCreate, PatientDisorderRead
from fastapi_app.database import get_db

router = APIRouter()

@router.get("/", response_model=list[PatientDisorderRead])
def read_all(db: Session = Depends(get_db)):
    return crud.get_all(db)

@router.post("/", response_model=PatientDisorderRead)
def create(obj_in: PatientDisorderCreate, db: Session = Depends(get_db)):
    return crud.create(db, obj_in)

@router.delete("/{patient_id}/{disorder_id}")
def delete(patient_id: int, disorder_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete(db, patient_id, disorder_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Record not found")
    return {"ok": True}

