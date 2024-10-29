from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.todo.dto.create_todo import CreateTodoDTO
from app.todo.dto.update_todo import UpdateTodoDTO
from app.todo.entities.todo import Todo
from app.database import get_db 
from app.todo.todo_service import TodoService

router = APIRouter()

@router.get("/todo")
async def get_todo(db: Session = Depends(get_db)):
    return TodoService(db).get_todo()

@router.post("/todo")
async def create_todo(todo_data: CreateTodoDTO, db: Session = Depends(get_db)):
    return TodoService(db).create_todo(todo_data)

@router.get("/todo/{todo_id}")
async def get_todo(todo_id: int, db: Session = Depends(get_db)):
    return TodoService(db).get_todo_by_id(todo_id)

@router.delete("/todo/{todo_id}")
async def get_todo(todo_id: int, db: Session = Depends(get_db)):
    return TodoService(db).deleted_todo(todo_id)

@router.put("/todo/{todo_id}")
async def get_todo(todo_id: int, todo_data: UpdateTodoDTO, db: Session = Depends(get_db)):
    return TodoService(db).update_todo(todo_id, todo_data)