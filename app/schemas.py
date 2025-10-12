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

class AppointmentStatusBase(BaseModel):
    status: str
    description: Optional[str] = None

class AppointmentStatusCreate(AppointmentStatusBase):
    pass

class AppointmentStatusOut(AppointmentStatusBase):
    id: int
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    role: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True

class DepartmentBase(BaseModel):
    name: str
    description: Optional[str] = None

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentOut(DepartmentBase):
    id: int
    class Config:
        orm_mode = True



class FeedbackBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_id: int
    rating: int
    comment: Optional[str] = None

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackOut(FeedbackBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True



class PaymentBase(BaseModel):
    appointment_id: int
    amount: int
    payment_status: Optional[str] = "pending"
    paid_at: Optional[datetime] = None

class PaymentCreate(PaymentBase):
    pass

class PaymentOut(PaymentBase):
    id: int
    class Config:
        orm_mode = True



class DoctorAvailabilityBase(BaseModel):
    doctor_id: int
    day_of_week: str
    start_time: str
    end_time: str

class DoctorAvailabilityCreate(DoctorAvailabilityBase):
    pass

class DoctorAvailabilityOut(DoctorAvailabilityBase):
    id: int
    class Config:
        orm_mode = True



class MedicalRecordBase(BaseModel):
    patient_id: int
    doctor_id: int
    diagnosis: Optional[str] = None
    prescription: Optional[str] = None

class MedicalRecordCreate(MedicalRecordBase):
    pass

class MedicalRecordOut(MedicalRecordBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True
