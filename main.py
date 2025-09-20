from fastapi import FastAPI
import uvicorn

app = FastAPI()

name_list = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
    {"id":4, "name": "abolfazl"},
    {"id":5, "name": "sara"},
    {"id":6, "name": "mehrshad"},
]
@app.get("/names")
async def retrive_names_list():
    return name_list

@app.post("/names")
async def add_name(name: str):
    new_id = len(name_list) + 1
    new_name = {"id": new_id, "name": name}
    name_list.append(new_name)
    return name_list