from pydantic import BaseModel


class Message(BaseModel):
    text: str


# Import pydantic: to define data models and validate input
# class Message(BaseModel): basemodal defines what kinda data is expected class Message = new blueprint called message
# text: str text must be a string
