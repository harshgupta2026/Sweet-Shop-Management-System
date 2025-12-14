from fastapi import FastAPI
from database import Base, engine
from auth import router as auth_router
from sweets import router as sweets_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sweet Shop Management System",
    description="Backend API for managing sweets, inventory, authentication and purchases",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(sweets_router)
