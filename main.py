from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4

app = FastAPI() # Create instances of API

tasks = []

class Task(BaseModel): #The given class definition is for a Task class which inherits from BaseModel. This class represents a task object with the following attributes:
    id: Optional[UUID] = None # An optional UUID. This could be used as a unique identifier for each task.
    title: str # A string representing the title of the task.
    description: Optional[str] = None # An optional string representing the description of the task.
    completed: bool = False
    #tags: List[str] = []

# Creating Post on API
@app.post("/tasks/", response_model=Task)
def creat_task(task: Task):
    task.id = uuid4()
    tasks.append(task)
    return task

@app.get("/tasks/", response_model=List[Task]) # send get reqyest to / URL
def read_tasks():
    return tasks

app.get("/tasks", response_model=Task)
def read_task(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            return task
    re


def read():
    return {"message": "Hello World"} # Return Hello World

if __name__ == "__main__": # 
    import uvicorn # Simple Web server

    uvicorn.run(app, host="0.0.0.0", port=8000)