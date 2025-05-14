from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_app import schemas, crud
from fastapi_app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Disorder)
def create_disorder(disorder: schemas.DisorderCreate, db: Session = Depends(get_db)):
    return crud.create_disorder(db=db, disorder=disorder)

@router.get("/", response_model=list[schemas.Disorder])
def read_disorders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_disorders(db=db, skip=skip, limit=limit)

@router.get("/{disorder_id}", response_model=schemas.Disorder)
def read_disorder(disorder_id: int, db: Session = Depends(get_db)):
    db_disorder = crud.get_disorder(db, disorder_id=disorder_id)
    if db_disorder is None:
        raise HTTPException(status_code=404, detail="Disorder not found")
    return db_disorder

@router.put("/{disorder_id}", response_model=schemas.Disorder)
def update_disorder(disorder_id: int, disorder: schemas.DisorderUpdate, db: Session = Depends(get_db)):
    db_disorder = crud.update_disorder(db, disorder_id=disorder_id, disorder=disorder)
    if db_disorder is None:
        raise HTTPException(status_code=404, detail="Disorder not found")
    return db_disorder

@router.delete("/{disorder_id}", response_model=schemas.Disorder)
def delete_disorder(disorder_id: int, db: Session = Depends(get_db)):
    db_disorder = crud.delete_disorder(db, disorder_id=disorder_id)
    if db_disorder is None:
        raise HTTPException(status_code=404, detail="Disorder not found")
    return db_disorder
