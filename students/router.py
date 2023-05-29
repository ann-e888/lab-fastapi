from fastapi import APIRouter, HTTPException

from students.schema import StudentCreateSchema, StudentUpdateSchema, Mark
from students.storage import *

router = APIRouter()

# @router.get("/")
# async def root():
#     return []

student_list = get_students_data()

@router.post("/", status_code = 200)
async def create_student(student:StudentCreateSchema):
    if student.first_name is not None and student.last_name is not None:
        student_list.append(student)
        return student
    raise HTTPException(
        status_code= 406,
        detail="Student must have name/surname"
    )


@router.put("/{student_id}")
async def update_student(student_id: int, student: StudentUpdateSchema):
    if student_id < 0 or student_id >= len(student_list):
        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )
    student_list[student_id] = student
    return student 

@router.get("/{student_id}")
async def get_students(student_id):
    return student_list[student_id]

@router.get("/")
async def get_student_list():
    return student_list

@router.delete("/{student_id}")
async def delete_student(student_id: int):
    if student_id < len(student_list):
        student_list.pop(student_id)
        raise HTTPException(status_code=200, detail="Student deleted")
    raise HTTPException(
        status_code=404,
        detail="Student can't be deleted because student doesn't exist"
    )

@router.post("/students/{student_id}/marks/{mark}")
async def addmark(id: int, mark : Mark):
    marks[id].append(mark.name)
    raise HTTPException(status_code=200, detail="Grade added")

@router.get("/{student_id}/marks")
async def getmark(student_id:int):
    if student_id in marks:
        return marks[student_id]
    raise HTTPException(status_code=404, detail="Student not found")

    