from enum import Enum
from typing import List
from pydantic import BaseModel

class Grade(float, Enum):
    BARDZO_DOBRY = 5.0
    DOBRY_PLUS = 4.5
    DOBRY = 4.0
    DOSTATECZNY_PLUS = 3.5
    DOSTATECZNY = 3.0
    NIEDOSTATECZNY = 2.0

class StudentBase():
    name : str 

class StudentCreateSchema(BaseModel):
    name : str

class StudentUpdateSchema(BaseModel):
    first_name: str | None

class Student(StudentBase):
    id: int
    name : str
    grades: List[Grade] = []