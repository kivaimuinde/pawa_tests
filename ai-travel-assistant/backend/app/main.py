# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import query

app = FastAPI(
    title="AI Travel Assistant",
    version="1.0.0"
)

# Allow your frontend domain during development
origins = [
    "http://localhost:3000",  # Next.js dev server
    "http://127.0.0.1:3000",  # Also common
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             # Use ["*"] for public APIs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query.router, prefix="/api/v1")
