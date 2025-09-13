from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
async def read_root():
    return {"foo": {read_item}}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/items/num/{item_num}")
async def read_item(item_num: int, q: Union[int, None] = None):
    return {item_num: item_num, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
