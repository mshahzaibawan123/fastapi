# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello! Welcome to Task API"}
# ---------------------------------------------------------
# from fastapi import FastAPI

# app = FastAPI(
#     title="Task CRUD API",
#     description="A simple Task Management API built with FastAPI",
#     version="1.0.0"
# )


# @app.get("/")
# def root():
#     return {
#         "message": "Welcome to the Task CRUD API",
#         "status": "Running"
#     }


# @app.get("/health")
# def health():
#     return {
#         "status": "healthy"
#     }
# ---------------------------------------------------------
# stage 2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Task CRUD API",
    description="A simple Task Management API built with FastAPI",
    version="1.0.0"
)


# -----------------------------
# Task Model
# -----------------------------
class Task(BaseModel):
    title: str
    description: str
    completed: bool = False


# -----------------------------
# In-Memory Database
# -----------------------------
tasks = []


# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def root():
    return {
        "message": "Welcome to the Task CRUD API",
        "status": "Running"
    }


# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# -----------------------------
# Get All Tasks
# -----------------------------
@app.get("/tasks")
def get_tasks():
    return tasks


# -----------------------------
# Get Task by ID
# -----------------------------
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")

    return tasks[task_id]


# -----------------------------
# Create a New Task
# -----------------------------
@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {
        "message": "Task created successfully",
        "task": task
    }

# -----------------------------
# Update Task
# -----------------------------
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")

    tasks[task_id] = updated_task

    return {
        "message": "Task updated successfully",
        "task": updated_task
    }

# -----------------------------
# Delete Task
# -----------------------------
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")

    deleted_task = tasks.pop(task_id)

    return {
        "message": "Task deleted successfully",
        "task": deleted_task
    }