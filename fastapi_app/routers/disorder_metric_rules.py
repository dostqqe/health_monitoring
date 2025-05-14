from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_app.crud import disorder_metric_rules as crud
from fastapi_app.schemas import disorder_metric_rules as schemas
from fastapi_app.database import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.DisorderMetricRule])
def read_all_rules(db: Session = Depends(get_db)):
    return crud.get_all_disorder_metric_rules(db)

@router.get("/{rule_id}", response_model=schemas.DisorderMetricRule)
def read_rule(rule_id: int, db: Session = Depends(get_db)):
    rule = crud.get_disorder_metric_rule(db, rule_id)
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")
    return rule

@router.post("/", response_model=schemas.DisorderMetricRule)
def create_rule(rule: schemas.DisorderMetricRuleCreate, db: Session = Depends(get_db)):
    return crud.create_disorder_metric_rule(db, rule)

@router.put("/{rule_id}", response_model=schemas.DisorderMetricRule)
def update_rule(rule_id: int, updated_rule: schemas.DisorderMetricRuleUpdate, db: Session = Depends(get_db)):
    rule = crud.update_disorder_metric_rule(db, rule_id, updated_rule)
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")
    return rule

@router.delete("/{rule_id}")
def delete_rule(rule_id: int, db: Session = Depends(get_db)):
    rule = crud.delete_disorder_metric_rule(db, rule_id)
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")
    return {"message": "Rule deleted"}
