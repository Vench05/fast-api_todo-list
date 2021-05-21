from multiprocessing.sharedctypes import Value
from fastapi import APIRouter, Depends, Form

from schema.todo import Todo
from fastapi.responses import RedirectResponse
import uuid

from database import get_db
from sqlalchemy.orm import Session

from models import Todo
from schema import todo

import json


router = APIRouter(
    tags=['Todo'],
    prefix='/todo'
)

@router.get("")
def todos(db: Session = Depends(get_db), limit: int = 10):
    return db.query(Todo).limit(limit).all()

@router.post("")
def add_todo(db: Session = Depends(get_db), name: str = Form(...)):
    todo = Todo(name=name)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return RedirectResponse(url=("/"), status_code=303)

@router.delete("/remove/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id==id).delete(synchronize_session=False)
    db.commit()
    return RedirectResponse(url=("/"), status_code=303)

@router.put("/update/{id}", response_model=todo.Todo)
def update_todo(id: int, body: dict, db: Session = Depends(get_db)):
    todo = db.query(Todo).get(id)
    todo.name = body['name']
    todo.done = body['done']
    db.commit()
    return todo