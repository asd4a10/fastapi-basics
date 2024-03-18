from enum import Enum
from fastapi import FastAPI
from todo import todo_router
from model import Item

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


@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


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
