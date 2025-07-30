# app/core/config.py
# This file stores app configuration and secrets (like API keys).
# We can load environment variables from a .env file here.
# For example: OpenAI API key, debug mode, allowed origins, etc.


from fastapi.middleware.cors import CORSMiddleware

def setupCors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# Import CORSMiddleware: handles cross-origin requests. Frontend/Backend.

# app.add_middleware, CORSMiddleware,: #enable cors for frontend/backend communication
# allow_origins=["*"]: accept requests from any domain
# allow_credentials=True: allows cookies and credentials
# allow_methods=["*"]: accept all HTTP methods. GET, POST...
# allow_headers=["*"]: accept all headers.