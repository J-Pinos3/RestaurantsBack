from fastapi import FastAPI
import asyncio

app = FastAPI()


async def fetch_user_data(user_id: int):
    await asyncio.sleep(1)
    return {"user_id": user_id, "name": "John Doe"}


async def fetch_transaction_history(user_id: int):
    await asyncio.sleep(2)
    return {"user_id": user_id, "transactions": ["purchase 1","purchase 2"]}


@app.get("/user/{user_id}")
async def async_example(user_id: int):
    user_data = await fetch_user_data(user_id)
    transaction_data = await fetch_transaction_history(user_id)
    return {**user_data, **transaction_data}
    