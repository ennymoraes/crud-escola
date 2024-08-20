from sqlalchemy.orm import Session
from . import models, schemas

def create_student(db: Session, student: schemas.StudentCreate) -> models.Student:
    """Cria um novo aluno no banco de dados."""
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session, skip: int = 0, limit: int = 10) -> list[models.Student]:
    """Obtém uma lista de alunos com paginação."""
    return db.query(models.Student).offset(skip).limit(limit).all()

def get_student(db: Session, student_id: int) -> models.Student:
    """Obtém um aluno específico pelo ID."""
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def delete_student(db: Session, student_id: int) -> None:
    """Deleta um aluno específico pelo ID."""
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
