from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_app import crud, models, schemas
from fastapi_app.database import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.DispensaryObservation])
def read_observations(db: Session = Depends(get_db)):
    return crud.dispensary_observation.get_all_observations(db)

@router.get("/{observation_id}", response_model=schemas.DispensaryObservation)
def read_observation(observation_id: int, db: Session = Depends(get_db)):
    observation = crud.dispensary_observation.get_observation_by_id(db, observation_id)
    if not observation:
        raise HTTPException(status_code=404, detail="Observation not found")
    return observation

@router.post("/", response_model=schemas.DispensaryObservation)
def create_observation(observation: schemas.DispensaryObservationCreate, db: Session = Depends(get_db)):
    return crud.dispensary_observation.create_observation(db, observation)

@router.put("/{observation_id}", response_model=schemas.DispensaryObservation)
def update_observation(observation_id: int, updated_data: schemas.DispensaryObservationUpdate, db: Session = Depends(get_db)):
    observation = crud.dispensary_observation.update_observation(db, observation_id, updated_data)
    if not observation:
        raise HTTPException(status_code=404, detail="Observation not found")
    return observation

@router.delete("/{observation_id}", response_model=schemas.DispensaryObservation)
def delete_observation(observation_id: int, db: Session = Depends(get_db)):
    observation = crud.dispensary_observation.delete_observation(db, observation_id)
    if not observation:
        raise HTTPException(status_code=404, detail="Observation not found")
    return observation
