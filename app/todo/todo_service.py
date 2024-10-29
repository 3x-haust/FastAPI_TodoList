from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.todo.dto.create_todo import CreateTodoDTO
from app.todo.dto.update_todo import UpdateTodoDTO
from app.todo.entities.todo import Todo


class TodoService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_todo(self):
        todo = self.db.query(Todo).all()
        
        if not todo:
            raise HTTPException(
                status_code=404,
                detail="Todos are not found"
            )
        
        return todo
    
    def get_todo_by_id(self, todo_id: int):
        todo = self.db.query(Todo).filter(Todo.id == todo_id).first()
        
        if not todo:
            raise HTTPException(
                status_code=404,
                detail="Todo is not found"
            )
        
        return todo
    
    def create_todo(self, todo_data: CreateTodoDTO):
        new_todo = Todo(
            title=todo_data.title,
            completed=True
        )

        self.db.add(new_todo)
        self.db.commit()
        self.db.refresh(new_todo)
        return new_todo
    
    def delete_todo(self, todo_id: int):
        todo = self.get_todo_by_id(todo_id)

        if not todo:
            raise HTTPException(
                status_code=404,
                detail="Todo is not found"
            )
        
        self.db.delete(todo)
        self.db.commit()
        return todo
    
    def update_todo(self, todo_id: int, todo_data: UpdateTodoDTO):
        todo = self.get_todo_by_id(todo_id)

        if not todo:
            raise HTTPException(
                status_code=404,
                detail="Todo is not found"
            )
        
        for key, value in todo_data.dict(exclude_unset=True).items():
            setattr(todo, key, value)
        
        self.db.commit()
        self.db.refresh(todo)
        return todo