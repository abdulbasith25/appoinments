from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Patient
class PatientCreate(BaseModel):
    name: str
    email: str

class PatientOut(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True

# Doctor
class DoctorCreate(BaseModel):
    name: str
    specialty: Optional[str] = None

class DoctorOut(BaseModel):
    id: int
    name: str
    specialty: Optional[str]
    class Config:
        orm_mode = True

# Appointment
class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    time: datetime

class AppointmentOut(BaseModel):
    id: int
    patient: PatientOut
    doctor: DoctorOut
    time: datetime
    done: bool
    class Config:
        orm_mode = True
