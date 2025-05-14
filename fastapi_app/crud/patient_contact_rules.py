from sqlalchemy.orm import Session
from fastapi_app import models, schemas


def get_rules(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PatientContactRule).offset(skip).limit(limit).all()

def get_rule(db: Session, rule_id: int):
    return db.query(models.PatientContactRule).filter(models.PatientContactRule.id == rule_id).first()

def create_rule(db: Session, rule: schemas.PatientContactRuleCreate):
    db_rule = models.PatientContactRule(**rule.dict())
    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    return db_rule

def update_rule(db: Session, rule_id: int, rule: schemas.PatientContactRuleUpdate):
    db_rule = db.query(models.PatientContactRule).filter(models.PatientContactRule.id == rule_id).first()
    if db_rule is None:
        return None
    for key, value in rule.dict(exclude_unset=True).items():
        setattr(db_rule, key, value)
    db.commit()
    db.refresh(db_rule)
    return db_rule

def delete_rule(db: Session, rule_id: int):
    db_rule = db.query(models.PatientContactRule).filter(models.PatientContactRule.id == rule_id).first()
    if db_rule is None:
        return None
    db.delete(db_rule)
    db.commit()
    return db_rule
