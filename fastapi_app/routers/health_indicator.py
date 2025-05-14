from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from  fastapi_app.database import get_db
import fastapi_app.crud.heath_indicator as crud
import  fastapi_app.schemas.health_indicator as schemas

router = APIRouter()

@router.get("/", response_model=list[schemas.HealthIndicator])
def read_health_indicators(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_health_indicators(db, skip=skip, limit=limit)

@router.get("/{health_indicator_id}", response_model=schemas.HealthIndicator)
def read_health_indicator(health_indicator_id: int, db: Session = Depends(get_db)):
    db_indicator = crud.get_health_indicator(db, health_indicator_id)
    if db_indicator is None:
        raise HTTPException(status_code=404, detail="Health indicator not found")
    return db_indicator

@router.post("/", response_model=schemas.HealthIndicator)
def create_health_indicator(health_indicator: schemas.HealthIndicatorCreate, db: Session = Depends(get_db)):
    return crud.create_health_indicator(db, health_indicator)

@router.put("/{health_indicator_id}", response_model=schemas.HealthIndicator)
def update_health_indicator(health_indicator_id: int, updates: schemas.HealthIndicatorUpdate, db: Session = Depends(get_db)):
    db_indicator = crud.update_health_indicator(db, health_indicator_id, updates)
    if db_indicator is None:
        raise HTTPException(status_code=404, detail="Health indicator not found")
    return db_indicator

@router.delete("/{health_indicator_id}", response_model=schemas.HealthIndicator)
def delete_health_indicator(health_indicator_id: int, db: Session = Depends(get_db)):
    db_indicator = crud.delete_health_indicator(db, health_indicator_id)
    if db_indicator is None:
        raise HTTPException(status_code=404, detail="Health indicator not found")
    return db_indicator


