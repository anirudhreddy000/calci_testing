from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a: float
    b: float


@app.get("/")
def home():
    return {"message": "happy calcualtion"}


@app.post("/add")
def add(nums: Numbers):
    return {"result": nums.a + nums.b}


@app.post("/sub")
def subtract(nums: Numbers):
    return {"result": nums.a - nums.b}


@app.post("/mul")
def multiply(nums: Numbers):
    return {"result": nums.a * nums.b}


@app.post("/div")
def divide(nums: Numbers):
    if nums.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"result": nums.a / nums.b}