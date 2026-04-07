from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from models.basemodel import Item
from datetime import datetime

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


@app.post("/items/", status_code= status.HTTP_201_CREATED  )
async def create_item(item: Item):

    response_data={
        "timestamp":datetime.now().isoformat(),
        "data": {"name":item.name, "price": item.price}
    }

    return  JSONResponse(content=response_data)


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item.price <= 0:
        raise HTTPException(status_code=400, detail="Price must be greater than 0")
    return { "item_id":item_id, "name":item.name, "price": item.price}
    


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return { "message":f"Item with id {item_id} has been deleted."}


#query parameters /items/?skip=5&limit=20
@app.get("/items/")
def read_items(skip:int =0, limit:int =10):
    return {"skip": skip, "limit": limit}


@app.get("/custom_headers/")
async def custom_headers():
    headers = { "X-Custom-Header":"MuCustomHeaderValue" }
    return JSONResponse(content={"message": "Custom headers example"}, headers=headers)


items = { "1":{"name":"Item 1", "price": 10} }
@app.get("/itemss/{item_id}")
async def read_item_by_id(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

