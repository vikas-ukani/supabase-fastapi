from fastapi import FastAPI
from app.supabase import callProfileAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Welcome"}


@app.get("/profile")
async def get_profile():
    response = callProfileAPI()
    return response
