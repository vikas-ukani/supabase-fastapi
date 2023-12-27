from fastapi import FastAPI
from app.supabase import callProfileAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index():
    return {"message": "Welcome"}


@app.get("/profile")
async def get_profile():
    response = callProfileAPI()
    return response
