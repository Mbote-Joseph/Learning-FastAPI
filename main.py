from fastapi import FastAPI

app=FastAPI()

# GET- Get data
# POST- create data
# PUT- Update data
# DELETE- Delete Item

students={
    1: {
        "name": "john",
        "age": 24,
        "class": "Computer Science"
    }
}

@app.get("/")
async def index():
    return {"name": "First Data"}

@app.get("/student/{student_id}")
def get_student(student_id: int):
    return students[student_id]
