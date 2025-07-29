# app/api/routes.py
# This file defines our API routes (endpoints).
# It's separated from main.py to keep things clean and organized.
# Instead of putting all routes in main.py, we group them in here and include them in main.py.

from fastapi import APIRouter
from app.models.models import Message # Import message from models

router = APIRouter() 

@router.post("/sendMessage")
def send_message(message: Message):
    return {"reply": "Ribbit Ribbit!"}

# Import fastapi: imports FastAPI framework to build the app
# router = APIRouter() Let's you organize routes separately from main app