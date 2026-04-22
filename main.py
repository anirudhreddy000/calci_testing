from fastapi import FastAPI, Query
import socket
import os

app = FastAPI()

# identifies which server handled the request
SERVER_ID = os.getenv("SERVER_ID", socket.gethostname())

@app.get("/")
def home():
    return {"message": "happy calculations!", "server": SERVER_ID}

@app.get("/health")
def health():
    return {
        "status": "ok",
        "server": SERVER_ID
    }

@app.get("/add")
def add(a: float = Query(...), b: float = Query(...)):
    return {
        "operation": "add",
        "result": a + b,
        "server": SERVER_ID
    }

@app.get("/sub")
def sub(a: float = Query(...), b: float = Query(...)):
    return {
        "operation": "sub",
        "result": a - b,
        "server": SERVER_ID
    }

@app.get("/mul")
def mul(a: float = Query(...), b: float = Query(...)):
    return {
        "operation": "mul",
        "result": a * b,
        "server": SERVER_ID
    }

@app.get("/div")
def div(a: float = Query(...), b: float = Query(...)):
    if b == 0:
        return {
            "error": "division by zero",
            "server": SERVER_ID
        }
    return {
        "operation": "div",
        "result": a / b,
        "server": SERVER_ID
    }