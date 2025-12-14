from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class SweetCreate(BaseModel):
    name: str
    category: str
    price: float
    quantity: int

class SweetOut(SweetCreate):
    id: int
    class Config:
        from_attributes = True
