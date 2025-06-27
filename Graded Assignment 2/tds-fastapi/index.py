from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load CSV data once at startup
STUDENTS = []
with open("q-fastapi.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert studentId to integer
        row["studentId"] = int(row["studentId"])
        STUDENTS.append(row)

@app.get("/")
async def root():
    return JSONResponse(content={"message": "Welcome to the Student API!"})

@app.get("/api")
async def get_students(request: Request):
    query_params = request.query_params.getlist("class")

    if not query_params:
        return { "students": STUDENTS }

    # Filter based on provided classes
    filtered = [s for s in STUDENTS if s["class"] in query_params]
    return { "students": filtered }