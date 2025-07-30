# tests/test_chat.py
# This file contains automated tests for our API endpoints.
# Tests help us make sure our backend responds correctly.
# For example, here we test that the /ping endpoint returns "pong".
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI backend!"}



def test_send_reply_message(): 
    data = {"text": "Ribbit there!"} 
    response = client.post("/sendMessage", json=data) 
    assert response.status_code == 200 
    assert response.json() == {"reply": "Ribbit Ribbit!"} 





# def test_send_reply_message(): // Declare function
    # data = {} // Message we are sending to server

    # response = client.post("/sendMessage", json=data) // Send the message to the server at "/sendMessage" in json.form
    # assert response.status_code == 200 // Check if the server responds with this status -> meaning everything is okay
    # assert response.json() == {"reply": "Ribbit Ribbit!"} // Check if the response matches -> Expected reply {"reply": "Ribbit Ribbit!"}
