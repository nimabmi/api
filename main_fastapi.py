from fastapi import FastAPI, HTTPException
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
def read_task(task_id: UUID): # send get reqyest to /tasks/{task_id} URL
    for task in tasks: # h is expected to be a UUID (Universally Unique Identifier). It loops through a list of tasks, checking if the id of each task matches the provided task_id. 
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found") # If a match is found, it returns the task. If no match is found after checking all tasks, 
# it returns an HTTPException with a status code of 404 and a detail message of "Task not found".    

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: UUID, task: Task):
    for idx, task in enumerate(tasks): # Enumerate in order to we want index as task
        if task.id == task_id:
            updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            tasks[idx] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: UUID):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(idx)
            
    raise HTTPException(status_code=404, detail="Task not found")



def read():
    return {"message": "Hello World"} # Return Hello World

if __name__ == "__main__": # 
    import uvicorn # Simple Web server

    uvicorn.run(app, host="0.0.0.0", port=8000)