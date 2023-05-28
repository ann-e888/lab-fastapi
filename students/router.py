from fastapi import APIRouter

from students.schema import StudentCreateSchema, StudentUpdateSchema
from students.storage import get_students_data

router = APIRouter()
@router.get("/")
async def root():
    return []

student_list = get_students_data()

@router.post("/", status_code = 200)
async def create_student(student:StudentCreateSchema):
    student_list.append(student)
    return student 

@router.put("/{student_id}")
async def update_student(student_id: int, student: StudentUpdateSchema):
    student_list[student_id] = student

@router.get("/{student_id}")
async def get_students(student_id):
    return student_list[student_id]

@router.get("/")
async def get_student_list():
    return student_list



    