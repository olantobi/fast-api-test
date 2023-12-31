
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/login")
def login(user: User):
    # ...
    # do some magic
    # ...
    return {"msg": "login successful"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/items")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return {"data": item_dict, "message": "OK"}
