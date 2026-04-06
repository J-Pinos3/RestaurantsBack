from fastapi import FastAPI
from models.basemodel import Item

app = FastAPI(
    title="My First FastAPI Application",
    description="This is a simple FastAPI application to demonstrate how to create an API endpoint.",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {"message":"Hello, FastAPi"}


# /items/42?detail=true
@app.get("/items/{item_id}")#item_id is captured from url path (#path parameter)
def read_item(item_id: int, detail:bool = False):
    if detail:
        return {"item_id":item_id,"detail":"Full item details"}
    return {"item_id": item_id}

@app.post("/items/")
def create_item(item: Item):
    return {"name":item.name, "price": item.price}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return { "item_id":item_id, "name":item.name, "price": item.price}
    

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return { "message":f"Item with id {item_id} has been deleted."}


#query parameters /items/?skip=5&limit=20
@app.get("/items/")
def read_items(skip:int =0, limit:int =10):
    return {"skip": skip, "limit": limit}




