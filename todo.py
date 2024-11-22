from fastapi import APIRouter,Path
from model import Item, Todo

todo_list:Todo = []

todo = APIRouter()

@todo.post("/todo")
def add_todo(todo:Todo):
    todo_list.append(todo)
    return{"message": "Added"}


@todo.get("/todo")
def show_todos():
       return {"todos": todo_list}


@todo.get("/todo/{todo_id}")
def show_one_todo(todo_id:int=Path(...,title="ID")):
      for todo in todo_list:
            if todo.id == todo_id:
                return{"todo":todo}
      return {"message": "ID doesn't exist"}


@todo.delete("/todo/{todo_id}")
def delete_one(todo_id:int=Path(...)):
    for i in range(len(todo_list)):
        todo = todo_list[i]
        if todo.id == todo_id:
            todo_list.pop(i)
            return{"message":"Deleted done"}
    return {"message": "ID doesn't exist"}


@todo.put("/todo/{todo_id}")
def modify(todo_id: int, todo: Todo):
    for i, existing_todo in enumerate(todo_list):
        if existing_todo.id == todo_id:
            todo_list[i].item.descripcion = todo.item.descripcion
            todo_list[i].item.status = todo.item.status
            return {"message": "Todo updated successfully"}
    return {"message": "ID doesn't exist"}

@todo.delete("/todo")
def delete_all():
        todo_list.clear()  
        return {"message": "All todos deleted successfully"}