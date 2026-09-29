from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import models

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(username: str, email: str, password: str, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # In real apps, hash the password using passlib/bcrypt
    new_user = models.User(username=username, email=email, hashed_password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user_id": new_user.id}

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == email, models.User.hashed_password == password).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": user.id}