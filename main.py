# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello! Welcome to Task API"}
# ---------------------------------------------------------
from fastapi import FastAPI

app = FastAPI(
    title="Task CRUD API",
    description="A simple Task Management API built with FastAPI",
    version="1.0.0"
)

