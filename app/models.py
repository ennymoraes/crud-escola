from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    first_semester_grade = Column(Float)
    second_semester_grade = Column(Float)
    teacher_name = Column(String)
    room_number = Column(String)
