from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == []

def test_create_student():
    student_data = {
        "first_name": "John", 
        "last_name": "Doe"
        }
    response = client.post("/students/", json=student_data)
    assert response.status_code == 200
    assert response.json() == student_data

def test_create_invalid_student():
    student_data = {"first_name": "John"}
    response = client.post("/students/", json=student_data)
    assert response.status_code == 422

def test_add_students():
    add_students=[
        {"first_name":"John",
         "last_name":"Doe"},
        {"first_name":"Ben",
         "last_name":"Doe"},
        {"first_name":"Jane",
         "last_name":"Doe"}
    ]

    for student in add_students:
        response = client.post("/students/", json=student)
        assert response.status_code == 200

