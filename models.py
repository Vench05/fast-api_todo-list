from xmlrpc.client import Boolean
from database import Base

from sqlalchemy import Column, Integer, String, Boolean

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True, unique=True)
    done = Column(Boolean)
