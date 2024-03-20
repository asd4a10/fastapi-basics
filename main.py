from enum import Enum
from fastapi import FastAPI, Query, Path
from todo import todo_router
from model import Item
from typing import List

app = FastAPI()

app.include_router(todo_router)


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.post("/")
async def post():
    return {"message": "Hello world from post route"}


@app.get("/user")
async def get_users():
    return {"users": []}


@app.get("/user/me")
async def get_user():
    return {"user_id": "current_user"}


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegs = "vegs"
    dairy = "dairy"


@app.get("/food/{food_name}")
async def get_user(food_name: FoodEnum):
    if food_name == FoodEnum.vegs:
        return {"food_name": food_name, "message": "healthy"}
    elif food_name == "fruits":
        return {"food_name": food_name, "message": "avg"}
    else:
        return {"food_name": food_name, "message": "not healt hy"}


fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Fool"},
    {"item_name": "Foko"},
    {"item_name": "Food"},
]


# @app.get("/items")
# async def list_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def get_user_item(item_id: str, q: str | None = None, short: bool = False):
    item = {
        "item_id": item_id,
    }
    if q:
        item.update({"q": q})
    if not short:
        item.update({"desc": "long long descr"})
    return item


@app.post("/items")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result


# Query(..., min_length=3, max_length=10)
# (q: List[str] = Query(["2", "5"]))
# (
#     q: str | None = Query(
#         None,
#         min_length=3,
#         max_length=10,
#         title="simple title",
#         description="sample description",
#         deprecated=True,
#     )
# )
@app.get("/items")
async def read_items(
    q: str | None = Query(
        None,
        min_length=3,
        max_length=10,
        title="simple title",
        description="sample description",
        alias="item-query",
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/hidden")
async def hidden_query_route(
    hidden_query: str | None = Query(None, include_in_schema=False)
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    return {"hidden_query": "Not found"}


@app.get("/numeric_validation/{item_id}")
async def numeric_validation_route(
    *,
    item_id: int = Path(..., title="id of the item", gt=10, le=100),
    q: str = "hello",
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
