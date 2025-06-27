from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, adjust as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods, adjust as needed
    allow_headers=["*"],  # Allows all headers, adjust as needed
)

@app.get("/")
def index():
    return {"message": "Hello, World!"}

@app.get("/api")
def search(request: Request):
    
    names_required = list(request.query_params.getlist("name"))
    marks_list = []
    
    with open("q-vercel-python.json", "r") as file:
        data = json.load(file)
    
    marks_data = {student['name']: student['marks'] for student in data}
    marks_list = [marks_data[name] for name in names_required]

    return{"marks": marks_list}