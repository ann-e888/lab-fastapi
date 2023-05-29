from functools import lru_cache
from students.schema import Mark


student_list = [{"first_name": "John",
                 "last_name": "Smith"}]

@lru_cache()
def get_students_data():
    return student_list

marks = {i: [] for i in range(len(student_list))}

@lru_cache()
def get_students_grades():
    return marks

