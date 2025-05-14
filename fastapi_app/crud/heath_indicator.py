from sqlalchemy.orm import Session
from fastapi_app.models import HealthIndicator
from fastapi_app.schemas import HealthIndicatorCreate, HealthIndicatorUpdate


def get_health_indicators(db: Session, skip: int = 0, limit: int = 100):
    return db.query(HealthIndicator).offset(skip).limit(limit).all()

def get_health_indicator(db: Session, health_indicator_id: int):
    return db.query(HealthIndicator).filter(HealthIndicator.id == health_indicator_id).first()

def create_health_indicator(db: Session, health_indicator: HealthIndicatorCreate):
    db_health_indicator = HealthIndicator(**health_indicator.dict())
    db.add(db_health_indicator)
    db.commit()
    db.refresh(db_health_indicator)
    return db_health_indicator

def update_health_indicator(db: Session, health_indicator_id: int, updates: HealthIndicatorUpdate):
    db_health_indicator = db.query(HealthIndicator).filter(HealthIndicator.id == health_indicator_id).first()
    if db_health_indicator is None:
        return None
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(db_health_indicator, field, value)
    db.commit()
    db.refresh(db_health_indicator)
    return db_health_indicator

def delete_health_indicator(db: Session, health_indicator_id: int):
    db_health_indicator = db.query(HealthIndicator).filter(HealthIndicator.id == health_indicator_id).first()
    if db_health_indicator is None:
        return None
    db.delete(db_health_indicator)
    db.commit()
    return db_health_indicator
