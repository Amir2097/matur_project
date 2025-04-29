from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.models import User
from app.schemas import UserOut
from app.crud import get_user

# Создаем базу данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Настроим CORS для работы с Nuxt
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/ping")
async def ping():
    return {"message": "Pong!"}

@app.get("/api/user/{user_id}", response_model=UserOut)
async def read_user(user_id: int, db: Depends(get_user)):
    return db
