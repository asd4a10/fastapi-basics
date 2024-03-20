"""
Lesson 7 onwards
"""

from fastapi import FastAPI, Query, Path, Body
from model import Item, Todo

app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., ge=0, le=100),
    item: Item | None = None,
    todo: Todo | None = None,
    importance: int = Body(...)
):
    results = {"item_id": item_id, "item": item, "todo": todo, "importance": importance}
    return results
