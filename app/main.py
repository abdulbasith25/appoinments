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


@app.get("/")
def home():
    return {"message": "FastAPI deployed successfully!"}
