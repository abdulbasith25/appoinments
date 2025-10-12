from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/medical_records", tags=["Medical Records"])
get_db = database.get_db

@router.post("/", response_model=schemas.MedicalRecordOut)
def create_medical_record(record: schemas.MedicalRecordCreate, db: Session = Depends(get_db)):
    db_record = models.MedicalRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

@router.get("/", response_model=list[schemas.MedicalRecordOut])
def list_medical_records(db: Session = Depends(get_db)):
    return db.query(models.MedicalRecord).all()
