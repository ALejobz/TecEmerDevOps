from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
import requests

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

url = 'https://62feef00a85c52ee483e5ca9.mockapi.io/items'

all_items = []

@app.get("/")
def read_root():
    
    response = requests.get(url, {}, timeout=5)
    all_items = response.json()
    return all_items


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/put")
def store_item(name: str, price: float , offer: bool, id_item):
    url_put = url + "/" + id_item
    item1 = {"name" : name, "price": price, "is_offer": offer}
    item_put = requests.put(url_put, json = item1)
    return item_put.json()

@app.delete("/del")
def del_item(id_item: str):
    url_del = url + "/" + id_item
    deleted = requests.delete(url_del)
    return deleted.json()

@app.post("/post")
def post_item(name: str, price: float , offer: bool):
    new_item = {"name" : name, "price": price, "is_offer": offer}
    item_post = requests.post(url, json = new_item)
    return item_post.json()

    




