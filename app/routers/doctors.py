from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/doctors", tags=["Doctors"])
get_db = database.get_db

@router.post("/", response_model=schemas.DoctorOut)
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    db_doctor = models.Doctor(name=doctor.name, specialty=doctor.specialty)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

@router.get("/", response_model=list[schemas.DoctorOut])
def list_doctors(db: Session = Depends(get_db)):
    return db.query(models.Doctor).all()
