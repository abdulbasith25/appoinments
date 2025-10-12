from fastapi import FastAPI
from . import models
from .database import engine
from .routers import patients, doctors, appointments

models.Base.metadata.create_all(bind=engine)  # Create tables

app = FastAPI(title="Doctor Appointment API")

# Include routers
app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(appointments.router)
app.include_router(departments.router)
app.include_router(users.router)
app.include_router(feedback.router)
app.include_router(payments.router)
app.include_router(doctor_availability.router)
app.include_router(medical_records.router)
app.include_router(appointment_status.router)


@app.get("/")
def home():
    return {"message": "FastAPI deployed successfully!"}
