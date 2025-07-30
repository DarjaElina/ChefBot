from fastapi import FastAPI
from app.api import routes
from app.core.config import setupCors

app = FastAPI()

setupCors(app)  # Call setupCors function

app.include_router(routes.router)  # Connect routes to routes file to main


# Import fastapi: imports FastAPI framework to build the app
# app = FastAPI(): creates the FastAPI app/web server
