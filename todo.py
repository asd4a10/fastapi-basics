from fastapi import APIRouter, Path
from model import Todo

todo_router = APIRouter()

todo_list = []


@todo_router.get("/todo")
async def get_todos():
    return {"todo_list": todo_list}


@todo_router.post("/todo")
async def add_todos(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "todo added successfully"}


@todo_router.get("/todo/{todo_id}")
async def get_todo_by_id(todo_id: int = Path(..., title="id of item to be retrieved")):
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"msg": "todo with given id not found"}
