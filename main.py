from fastapi import FastAPI, Path
from typing import Union


app=FastAPI()

# GET- Get data
# POST- create data
# PUT- Update data
# DELETE- Delete Item

students={
    1: {
        "name": "Joseph Mbote",
        "age": 24,
        "class": "Computer Science"
    }

}

@app.get("/")
async def index():
    return {"name": "First Data"}

@app.get("/student/{student_id}")
def get_student(student_id: int=Path(None, description="The ID of the student you want to view")):
    return students[student_id]

@app.get("/student-by-name")
def get_student_by_name(name: str=Path(None, description="The name of the student")):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data": "Not Found"}

@app.post('post-student')
def post_student(student_id: int=Path(None, description="The ID of the student you want to view")):
    return students[student_id]


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item