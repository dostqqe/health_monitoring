from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_app import crud, models, schemas
from fastapi_app.database import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.MetricType])
def read_metric_types(db: Session = Depends(get_db)):
    return crud.get_metric_types(db)

@router.get("/{metric_type_id}", response_model=schemas.MetricType)
def read_metric_type(metric_type_id: int, db: Session = Depends(get_db)):
    db_metric_type = crud.get_metric_type(db, metric_type_id)
    if db_metric_type is None:
        raise HTTPException(status_code=404, detail="Metric type not found")
    return db_metric_type

@router.post("/", response_model=schemas.MetricType)
def create_metric_type(metric_type: schemas.MetricTypeCreate, db: Session = Depends(get_db)):
    return crud.create_metric_type(db, metric_type)

@router.put("/{metric_type_id}", response_model=schemas.MetricType)
def update_metric_type(metric_type_id: int, metric_type: schemas.MetricTypeUpdate, db: Session = Depends(get_db)):
    return crud.update_metric_type(db, metric_type_id, metric_type)

@router.delete("/{metric_type_id}")
def delete_metric_type(metric_type_id: int, db: Session = Depends(get_db)):
    return crud.delete_metric_type(db, metric_type_id)
