from pydantic import BaseModel
import uuid

def get_new_id() -> str:
    return str(uuid.uuid4())[:5]

class Todo(BaseModel):
    id: str = get_new_id()
    name: str
    done: bool = False
    
