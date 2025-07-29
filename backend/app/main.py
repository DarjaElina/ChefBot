# app/main.py
# This is the main entry point of the FastAPI backend.
# It creates the app instance and includes all route files.
# We run this file using `uvicorn` to start the server.


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI backend!"}
