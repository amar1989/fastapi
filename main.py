from http.client import HTTPException
from pathlib import Path

from fastapi import FastAPI,Depends
from fastapi.openapi.utils import status_code_ranges
from starlette import status

import models
from models import Todos
from database import engine, SessionLocal
from fastapi import FastAPI
from database import engine, SessionLocal
from typing import Annotated
from sqlalchemy import orm
from sqlalchemy.orm import Session

app=FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_all(db:Annotated[Session,Depends(get_db)]):
    return db.query(Todos).all()

@app.get("/todo/{todo_id}",status_code=status.HTTP_200_OK)
async def read_todo(db: Annotated[Session,Depends(get_db)],todo_id:int=Path(gt=0)):
    todo_model=db.query(Todos).filter(Todos.id  == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail='Todo not found')


