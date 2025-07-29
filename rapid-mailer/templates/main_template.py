from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Email Service")

app.include_router(router)