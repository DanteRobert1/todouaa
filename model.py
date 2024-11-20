from pydantic import BaseModel

class Item(BaseModel):
        descripcion:str
        status:str

class Todo(BaseModel):
        id:int 
        item:Item