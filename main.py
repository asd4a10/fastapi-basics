from enum import Enum
from fastapi import FastAPI
from todo import todo_router

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
