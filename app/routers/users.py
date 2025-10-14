from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database, security

router = APIRouter(prefix="/users", tags=["Users"])
get_db = database.get_db

# Create a new user with hashed password
@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # check if username or email already exists
    if db.query(models.User).filter(models.User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        password=hashed_password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# List all users (optionally protect with JWT)
@router.get("/", response_model=list[schemas.UserOut])
def list_users(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(security.get_current_user)  # JWT protected
):
    return db.query(models.User).all()















# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from .. import models, schemas, database

# router = APIRouter(prefix="/users", tags=["Users"])
# get_db = database.get_db

# @router.post("/", response_model=schemas.UserOut)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = models.User(**user.dict())
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# @router.get("/", response_model=list[schemas.UserOut])
# def list_users(db: Session = Depends(get_db)):
#     return db.query(models.User).all()
