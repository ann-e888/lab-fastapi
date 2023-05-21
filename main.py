from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

class StudentUpdateSchema(BaseModel):
    first_name: str | None
    last_name: str | None

student_list = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/students/", status_code = 200)
async def create_student(student:StudentCreateSchema):
    student_list.append(student)
    return student 

@app.put("/student/{student_id}")
async def update_student(student_id: int, student: StudentUpdateSchema):
    student_list[student_id] = student

@app.get("/student/{student_id}")
async def get_student(student_id: int):
    return {"student_info": student_list[student_id]}