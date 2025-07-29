from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes # Import from routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router) # Connect routes to routes file to main


# Import fastapi: imports FastAPI framework to build the app
# Import CORSMiddleware: handles cross-origin requests. Frontend/Backend.

# app = FastAPI(): creates the FastAPI app/web server
# app.add_middleware, CORSMiddleware,: #enable cors for frontend/backend communication
# allow_origins=["*"]: accept requests from any domain
# allow_credentials=True: allows cookies and credentials
# allow_methods=["*"]: accept all HTTP methods. GET, POST...
# allow_headers=["*"]: accept all headers.