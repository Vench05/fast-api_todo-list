from fastapi import APIRouter, Form
from schema.todo import Todo
from fastapi.responses import RedirectResponse
import uuid


router = APIRouter()

todo_list = []


@router.get("/todo", tags=["Todo"])
def todos():
    return todo_list

@router.post("/todo", tags=["Todo"])
def add_todo(name: str = Form(...)):
    todo_list.append(Todo(name=name, id=str(uuid.uuid4())[:5]).__dict__)
    return RedirectResponse(url=("/"), status_code=303)

@router.delete("/todo/remove/{id}", tags=["Todo"])
def delete_todo(id: str):
    global todo_list
    new_todo = todo_list.copy()
    new_todo = [i for i in new_todo if i["id"] != id]
    todo_list = new_todo
    return RedirectResponse(url=("/"), status_code=303)

@router.put("/todo/update/{id}", tags=["Todo"])
def update_todo(id: str, body: dict):
    global todo_list
    new_todo = todo_list.copy()
    new_todo = [i if i["id"] != id else body for i in new_todo]
    # new_todo.append(body)
    todo_list = new_todo
    return todo_list
