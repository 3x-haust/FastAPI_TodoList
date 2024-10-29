from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.database import engine, Base
from app.todo.todo_controller import router as todo_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo_router, prefix="/api")