from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    age: int
    first_semester_grade: float
    second_semester_grade: float
    teacher_name: str
    room_number: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True
