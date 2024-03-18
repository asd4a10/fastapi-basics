from fastapi import APIRouter, Path
from model import Todo, TodoItem
from typing import List

todo_router = APIRouter()

todo_list: List[Todo] = []


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


@todo_router.put("/todo/{todo_id}")
async def update_todo_by_id(
    new_todo: TodoItem, todo_id: int = Path(..., title="id of item to be retrieved")
):
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = new_todo.item
            return {"msg": "todo was updated!"}
    return {"msg": "todo with given id not found"}


@todo_router.delete("/todo/{todo_id}")
async def delete_todo_by_id(
    todo_id: int = Path(..., title="id of item to be retrieved")
):
    for index in range(len(todo_list)):
        if todo_list[index] == todo_id:
            todo_list.pop(index)
            return {"msg": "todo was deleted!"}
    return {"msg": "todo with given id not found"}


@todo_router.delete("/todo")
async def clear_todo_list():
    todo_list.clear()
    return {"msg": "todo list was cleared"}
