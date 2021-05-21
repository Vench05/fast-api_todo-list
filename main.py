from urllib import request
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from api import todo
from database import get_db, engine
import models

from sqlalchemy.orm import Session

from models import Todo

templates = Jinja2Templates(directory="templates")


app = FastAPI()


models.Base.metadata.create_all(engine)

app.include_router(todo.router)
app.mount("/static", StaticFiles(directory="static"), name='static')

@app.get("/", response_class=HTMLResponse, tags=['pages'])
def index(req: Request, db: Session = Depends(get_db), limit: int =10):
    return templates.TemplateResponse("home.html", {"request": req, "data": db.query(Todo).limit(limit).all()})

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)