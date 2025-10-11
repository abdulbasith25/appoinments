from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/appointments", tags=["Appointments"])
get_db = database.get_db

@router.post("/", response_model=schemas.AppointmentOut)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == appointment.patient_id).first()
    doctor = db.query(models.Doctor).filter(models.Doctor.id == appointment.doctor_id).first()
    if not patient or not doctor:
        raise HTTPException(status_code=404, detail="Patient or Doctor not found")
    
    db_appointment = models.Appointment(patient_id=appointment.patient_id,
                                        doctor_id=appointment.doctor_id,
                                        time=appointment.time)
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

@router.get("/", response_model=list[schemas.AppointmentOut])
def list_appointments(db: Session = Depends(get_db)):
    return db.query(models.Appointment).all()
