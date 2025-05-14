from sqlalchemy.orm import Session
from fastapi_app import models, schemas


def get_metric_types(db: Session):
    return db.query(models.MetricType).all()

def get_metric_type(db: Session, metric_type_id: int):
    return db.query(models.MetricType).filter(models.MetricType.id == metric_type_id).first()

def create_metric_type(db: Session, metric_type: schemas.MetricTypeCreate):
    db_metric_type = models.MetricType(**metric_type.dict())
    db.add(db_metric_type)
    db.commit()
    db.refresh(db_metric_type)
    return db_metric_type

def update_metric_type(db: Session, metric_type_id: int, metric_type: schemas.MetricTypeUpdate):
    db_metric_type = db.query(models.MetricType).filter(models.MetricType.id == metric_type_id).first()
    if db_metric_type:
        for field, value in metric_type.dict(exclude_unset=True).items():
            setattr(db_metric_type, field, value)
        db.commit()
        db.refresh(db_metric_type)
    return db_metric_type

def delete_metric_type(db: Session, metric_type_id: int):
    db_metric_type = db.query(models.MetricType).filter(models.MetricType.id == metric_type_id).first()
    if db_metric_type:
        db.delete(db_metric_type)
        db.commit()
    return db_metric_type
