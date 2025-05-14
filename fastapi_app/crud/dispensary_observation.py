from sqlalchemy.orm import Session
from fastapi_app import models, schemas


def get_all_observations(db: Session):
    return db.query(models.DispensaryObservation).all()

def get_observation_by_id(db: Session, observation_id: int):
    return db.query(models.DispensaryObservation).filter(models.DispensaryObservation.id == observation_id).first()

def create_observation(db: Session, observation: schemas.DispensaryObservationCreate):
    db_observation = models.DispensaryObservation(**observation.dict())
    db.add(db_observation)
    db.commit()
    db.refresh(db_observation)
    return db_observation

def update_observation(db: Session, observation_id: int, updated_data: schemas.DispensaryObservationUpdate):
    db_observation = db.query(models.DispensaryObservation).filter(models.DispensaryObservation.id == observation_id).first()
    if db_observation:
        for key, value in updated_data.dict(exclude_unset=True).items():
            setattr(db_observation, key, value)
        db.commit()
        db.refresh(db_observation)
    return db_observation

def delete_observation(db: Session, observation_id: int):
    db_observation = db.query(models.DispensaryObservation).filter(models.DispensaryObservation.id == observation_id).first()
    if db_observation:
        db.delete(db_observation)
        db.commit()
    return db_observation
