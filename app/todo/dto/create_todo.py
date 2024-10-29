from pydantic import BaseModel

class CreateTodoDTO(BaseModel):
    title: str
