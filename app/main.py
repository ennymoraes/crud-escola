from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

# Cria todas as tabelas no banco de dados
models.Base.metadata.create_all(bind=database.engine)

# Instancia a aplicação FastAPI
app = FastAPI()

# Endpoint para criar um novo aluno
@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(database.get_db)):
    return crud.create_student(db=db, student=student)

# Endpoint para listar todos os alunos com paginação
@app.get("/students/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_students(db, skip=skip, limit=limit)

# Endpoint para ler as informações de um aluno específico
@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(database.get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

# Endpoint para deletar um aluno específico
@app.delete("/students/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(database.get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    crud.delete_student(db, student_id=student_id)
    return db_student
