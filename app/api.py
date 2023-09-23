from fastapi import FastAPI
from message import Message

app = FastAPI()


@app.get("/greeting")
async def greeting_world():
    """
    Greet the world
    """
    return {"greeting": "Hello, world!"}


@app.get("/greeting/{name}")
async def greeting(name: str):
    """
    Greet the user:

    **Path params**:
    - **name**: username
    """
    return {"greeting": f"Hello, {name}!"}


@app.get("/biography")
async def biography(name: str, age: int = None, location: str = None):
    """
    Create a biography from data:

    **Query params**:
    - **name**: username
    - **age**: user age
    - **location**: user location
    """
    info = f"I'm {name}."
    if age:
        info += f" I'm {age} years old."
    if location:
        info += f" I'm from {location}."
    return {"biography": info}


@app.post("/message/{group_id}")
async def message(group_id: int, message: Message):
    """
    Send a message to the group:

    **Body parameters**:
    - **name**: message sender name
    - **text**: message text
    """
    return {"group_id": group_id, "message": message}
