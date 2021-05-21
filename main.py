from urllib import request
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import db

from api import todo

templates = Jinja2Templates(directory="templates")


app = FastAPI()

#connect to database on startup



app.include_router(todo.router)
app.mount("/static", StaticFiles(directory="static"), name='static')


@app.get("/", response_class=HTMLResponse, tags=['pages'])
def index(req: Request):
    return templates.TemplateResponse("home.html", {"request": req, "data": todo.todo_list})

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)