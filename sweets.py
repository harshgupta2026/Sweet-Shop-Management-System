from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Sweet
from schemas import SweetCreate
from deps import get_current_user, admin_only

router = APIRouter(prefix="/api/sweets")

@router.post("")
def add_sweet(data: SweetCreate, user=Depends(get_current_user)):
    db = SessionLocal()
    sweet = Sweet(**data.dict())
    db.add(sweet)
    db.commit()
    return sweet

@router.get("")
def list_sweets():
    db = SessionLocal()
    return db.query(Sweet).all()

@router.get("/search")
def search(name: str = None, category: str = None, min_price: float = None, max_price: float = None):
    db = SessionLocal()
    q = db.query(Sweet)
    if name:
        q = q.filter(Sweet.name.contains(name))
    if category:
        q = q.filter(Sweet.category == category)
    if min_price is not None:
        q = q.filter(Sweet.price >= min_price)
    if max_price is not None:
        q = q.filter(Sweet.price <= max_price)
    return q.all()

@router.put("/{id}")
def update(id: int, data: SweetCreate, user=Depends(get_current_user)):
    db = SessionLocal()
    sweet = db.query(Sweet).get(id)
    if not sweet:
        raise HTTPException(404)
    for k, v in data.dict().items():
        setattr(sweet, k, v)
    db.commit()
    return sweet

@router.delete("/{id}")
def delete(id: int, user=Depends(admin_only)):
    db = SessionLocal()
    sweet = db.query(Sweet).get(id)
    if not sweet:
        raise HTTPException(404)
    db.delete(sweet)
    db.commit()
    return {"deleted": True}

@router.post("/{id}/purchase")
def purchase(id: int, user=Depends(get_current_user)):
    db = SessionLocal()
    sweet = db.query(Sweet).get(id)
    if sweet.quantity <= 0:
        raise HTTPException(400)
    sweet.quantity -= 1
    db.commit()
    return sweet

@router.post("/{id}/restock")
def restock(id: int, qty: int, user=Depends(admin_only)):
    db = SessionLocal()
    sweet = db.query(Sweet).get(id)
    sweet.quantity += qty
    db.commit()
    return sweet
