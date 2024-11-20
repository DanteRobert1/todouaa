from fastapi import FastAPI
from todo import todo

app = FastAPI()

@app.get("/")
def home():
    return "Bienvenido"

@app.get("/name/{name}")
def greeting(name:str):
    return "Hola"+ name

app.include_router(todo)
