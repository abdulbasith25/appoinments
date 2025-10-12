from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/payments", tags=["Payments"])
get_db = database.get_db

@router.post("/", response_model=schemas.PaymentOut)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    db_payment = models.Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

@router.get("/", response_model=list[schemas.PaymentOut])
def list_payments(db: Session = Depends(get_db)):
    return db.query(models.Payment).all()
