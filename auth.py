from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from schemas import UserCreate, UserLogin
from security import hash_password, verify_password, create_token

router = APIRouter(prefix="/api/auth")

@router.post("/register")
def register(data: UserCreate):
    db: Session = SessionLocal()
    try:
        if db.query(User).filter(User.email == data.email).first():
            raise HTTPException(status_code=400, detail="User already exists")
        user = User(
            email=data.email,
            password=hash_password(data.password),
            is_admin=False
        )
        db.add(user)
        db.commit()
        return {"status": "registered"}
    finally:
        db.close()

@router.post("/login")
def login(data: UserLogin):
    db: Session = SessionLocal()
    try:
        user = db.query(User).filter(User.email == data.email).first()
        if not user or not verify_password(data.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        token = create_token({"id": user.id})
        return {"access_token": token, "token_type": "bearer"}
    finally:
        db.close()
