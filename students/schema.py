from pydantic import BaseModel
from enum import Enum


class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

class StudentUpdateSchema(BaseModel):
    first_name: str | None
    last_name: str | None

class Mark(str, Enum):
    BARDZO_DOBRY = 5.0
    DOBRY_PLUS = 4.5
    DOBRY = 4.0
    DOSTATECZNY_PLUS = 3.5
    DOSTATECZNY = 3.0
    NIEDOSTATECZNY = 2.0