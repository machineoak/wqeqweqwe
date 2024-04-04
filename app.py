from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"foo": {read_item}}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/items/num/{item_num}")
async def read_item(item_num: int, q: Union[int, None] = None):
    return {item_num: item_num, "q": q}