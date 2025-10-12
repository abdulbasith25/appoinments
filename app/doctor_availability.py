from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/doctor_availability", tags=["Doctor Availability"])
get_db = database.get_db

@router.post("/", response_model=schemas.DoctorAvailabilityOut)
def create_doctor_availability(data: schemas.DoctorAvailabilityCreate, db: Session = Depends(get_db)):
    db_data = models.DoctorAvailability(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

@router.get("/", response_model=list[schemas.DoctorAvailabilityOut])
def list_doctor_availability(db: Session = Depends(get_db)):
    return db.query(models.DoctorAvailability).all()
