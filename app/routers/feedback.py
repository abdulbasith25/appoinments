from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/feedback", tags=["Feedback"])
get_db = database.get_db

@router.post("/", response_model=schemas.FeedbackOut)
def create_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    db_feedback = models.Feedback(**feedback.dict())
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

@router.get("/", response_model=list[schemas.FeedbackOut])
def list_feedback(db: Session = Depends(get_db)):
    return db.query(models.Feedback).all()
