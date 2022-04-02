from fastapi import FastAPI, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import Base, ToDo, engine


# Create ToDoRequest Base Model
class ToDoRequest(BaseModel):
    task: str


# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()


@app.get("/")
def root():
    return "todooo"


@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo(todo: ToDoRequest):
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # create an instance of the ToDo database model
    tododb = ToDo(task=todo.task)

    session.add(tododb)
    session.commit()

    id = tododb.id

    session.close()

    return f"created todo item with id {id}"


@app.get("/todo/{id}")
def read_todo(id: int):
    return "read todo item with id {id}"


@app.put("/todo/{id}")
def update_todo(id: int):
    return "update todo item with id {id}"


@app.delete("/todo/{id}")
def delete_todo(id: int):
    return "delete todo item with id {id}"


@app.get("/todo")
def read_todo_list():
    return "read todo list"
