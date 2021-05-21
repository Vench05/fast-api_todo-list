from typing import List
import sqlalchemy
import databases

DATABASE_URL = "sqlite:///./todo.db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

#Table of todos
todos = sqlalchemy.Table(
    "todos",
    metadata,
    sqlalchemy.Column("id",  sqlalchemy.Integer, primary_key = True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("done", sqlalchemy.Boolean),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args = {"check_same_thread": False})
metadata.create_all(engine)
