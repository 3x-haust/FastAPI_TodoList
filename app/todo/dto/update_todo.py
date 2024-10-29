from pydantic import BaseModel

class UpdateTodoDTO(BaseModel):
    title: str
    completed: bool