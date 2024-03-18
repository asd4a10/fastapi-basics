from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {"example": {"item": "Example item 1"}}


class Item(BaseModel):
    name: str
    description: str | None = None
    price: int
    tax: float | None = None
