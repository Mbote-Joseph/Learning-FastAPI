from fastapi import FastAPI

app=FastAPI()

# GET- Get data
# POST- create data
# PUT- Update data
# DELETE- Delete Item

@app.get("/")
async def root():
    return {"message": "Hello World"}

