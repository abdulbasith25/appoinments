from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/appointment_status", tags=["Appointment Status"])
get_db = database.get_db

@router.post("/", response_model=schemas.AppointmentStatusOut)
def create_appointment_status(status: schemas.AppointmentStatusCreate, db: Session = Depends(get_db)):
    db_status = models.AppointmentStatus(**status.dict())
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status

@router.get("/", response_model=list[schemas.AppointmentStatusOut])
def list_appointment_statuses(db: Session = Depends(get_db)):
    return db.query(models.AppointmentStatus).all()
