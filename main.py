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