from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)

    appointments = relationship("Appointment", back_populates="patient")

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialty = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    appointments = relationship("Appointment", back_populates="doctor")
    
    department = relationship("Department")

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    time = Column(DateTime, default=datetime.datetime.utcnow)
    done = Column(Boolean, default=False)

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")

class AppointmentStatus(Base):
    __tablename__ = "appointment_status"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    description = Column(String)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False) 
    role = Column(String, nullable=False) 


class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)


class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=False)
    rating = Column(Integer, nullable=False)  # 1 to 5
    comment = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    patient = relationship("Patient")
    doctor = relationship("Doctor")
    appointment = relationship("Appointment")


class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"))
    amount = Column(Integer, nullable=False)
    payment_status = Column(String, default="pending")  # paid, pending, failed
    paid_at = Column(DateTime)

    appointment = relationship("Appointment")


class DoctorAvailability(Base):
    __tablename__ = "doctor_availability"
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    day_of_week = Column(String, nullable=False)  # e.g., "Monday"
    start_time = Column(String, nullable=False)   # "09:00"
    end_time = Column(String, nullable=False)     # "17:00"

    doctor = relationship("Doctor")


class MedicalRecord(Base):
    __tablename__ = "medical_records"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    diagnosis = Column(String)
    prescription = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    patient = relationship("Patient")
    doctor = relationship("Doctor")
