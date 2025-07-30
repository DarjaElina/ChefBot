# app/api/routes.py
# This file defines our API routes (endpoints).
# It's separated from main.py to keep things clean and organized.
# Instead of putting all routes in main.py, we group them in here and include them in main.py.

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Message(BaseModel):
    text: str

@router.get("/") # Root route
def root():
    return {"message": "Hello from FastAPI backend!"}

@router.post("/sendMessage")
def send_message(message: Message):
    return {"reply": "Ribbit Ribbit!"}


# Import fastapi: imports FastAPI framework to build the app
# router = APIRouter() Let's you organize routes separately from main app

# @router.post("/sendMessage"): Define endpoint to /sendMessage
# def send_message(message: Message): Define function that get called when Post request is sent 

