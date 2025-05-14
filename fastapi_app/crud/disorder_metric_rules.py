from sqlalchemy.orm import Session
from fastapi_app.models import DisorderMetricRule
from fastapi_app.schemas.disorder_metric_rules import DisorderMetricRuleCreate, DisorderMetricRuleUpdate


def get_all_disorder_metric_rules(db: Session):
    return db.query(DisorderMetricRule).all()

def get_disorder_metric_rule(db: Session, rule_id: int):
    return db.query(DisorderMetricRule).filter(DisorderMetricRule.id == rule_id).first()

def create_disorder_metric_rule(db: Session, rule: DisorderMetricRuleCreate):
    db_rule = DisorderMetricRule(**rule.model_dump())
    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    return db_rule

def update_disorder_metric_rule(db: Session, rule_id: int, updated_rule: DisorderMetricRuleUpdate):
    db_rule = db.query(DisorderMetricRule).filter(DisorderMetricRule.id == rule_id).first()
    if db_rule:
        for field, value in updated_rule.model_dump(exclude_unset=True).items():
            setattr(db_rule, field, value)
        db.commit()
        db.refresh(db_rule)
    return db_rule

def delete_disorder_metric_rule(db: Session, rule_id: int):
    db_rule = db.query(DisorderMetricRule).filter(DisorderMetricRule.id == rule_id).first()
    if db_rule:
        db.delete(db_rule)
        db.commit()
    return db_rule
