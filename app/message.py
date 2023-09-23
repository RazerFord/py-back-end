from pydantic import BaseModel


class Message(BaseModel):
    """User message"""
    name: str
    text: str
