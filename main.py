from fastapi import FastAPI, Path

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
