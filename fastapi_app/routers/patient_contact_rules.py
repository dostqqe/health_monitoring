from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_app import crud, schemas
from fastapi_app.database import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.PatientContactRule])
def read_rules(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.patient_contact_rules.get_rules(db, skip=skip, limit=limit)

@router.get("/{rule_id}", response_model=schemas.PatientContactRule)
def read_rule(rule_id: int, db: Session = Depends(get_db)):
    db_rule = crud.patient_contact_rules.get_rule(db, rule_id)
    if db_rule is None:
        raise HTTPException(status_code=404, detail="Rule not found")
    return db_rule

@router.post("/", response_model=schemas.PatientContactRule)
def create_rule(rule: schemas.PatientContactRuleCreate, db: Session = Depends(get_db)):
    return crud.patient_contact_rules.create_rule(db, rule)

@router.put("/{rule_id}", response_model=schemas.PatientContactRule)
def update_rule(rule_id: int, rule: schemas.PatientContactRuleUpdate, db: Session = Depends(get_db)):
    db_rule = crud.patient_contact_rules.update_rule(db, rule_id, rule)
    if db_rule is None:
        raise HTTPException(status_code=404, detail="Rule not found")
    return db_rule

@router.delete("/{rule_id}", response_model=schemas.PatientContactRule)
def delete_rule(rule_id: int, db: Session = Depends(get_db)):
    db_rule = crud.patient_contact_rules.delete_rule(db, rule_id)
    if db_rule is None:
        raise HTTPException(status_code=404, detail="Rule not found")
    return db_rule
