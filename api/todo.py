from typing import List
from fastapi import APIRouter, Form
from schema.todo import Todo
import db.database as data_b
from fastapi.responses import RedirectResponse
import uuid

router = APIRouter()

todo_list = []


@router.on_event("startup")
async def startup():
    if not data_b.database.is_connected:
        await data_b.database.connect()

@router.on_event("shutdown")
async def shutdown():
    if data_b.database.is_connected:
        await data_b.database.disconnect()

#now it needs to be a assyncronous function and we will use some news .
# the response_model parameters shows that the response will be a list of Todo type

@router.get("/todo", response_model = List[Todo])
async def todos():
    #get Todos from database table named as todos
    query = data_b.todos.select()
    return await data_b.database.fetch_all(query)
    # return todo_list

@router.post("/todo",)
def add_todo(name: str):
    todo_list.append(Todo(name=name, id=str(uuid.uuid4())[:5]).__dict__)
    
    return RedirectResponse(url=("/"), status_code=303)
    # todo = Todo(name = name, id = uuid.uuid4, done = False)
    # query = data_b.todos.insert().values(id = todo., name = todo["name"], done = todo["done"])
    # return {**todo}

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
