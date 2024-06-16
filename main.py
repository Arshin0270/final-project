from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()


@app.post("/createcourse/", response_model=schemas.course)
def create_course(course: schemas.course, db: Session = Depends(get_db)):
    db_course = crud.get_course(db=db,course_id=course.CID) 
    if db_course:
        raise HTTPException(status_code=400, detail="course already exists")
    return crud.create_course(db=db, course=course)

@app.post("/createteacher/", response_model=schemas.teacher)
def create_teacher(teacher:schemas.teacher,db:Session=Depends(get_db)):
    db_teacher=crud.get_teacher(db=db,teacher_id=teacher.LID)
    if db_teacher!=None:
        raise HTTPException(status_code=400,detail='teacher already exists')
    return crud.create_teacher(db=db,teacher=teacher)

@app.post("/createstudent/", response_model=schemas.student)
def create_student(student:schemas.student,db:Session=Depends(get_db)):
    db_student=crud.get_student(db=db,student_id=student.STID)
    if db_student!=None:
        raise HTTPException(status_code=400,detail='student already exists')
    return crud.create_student(student=student,db=db)

@app.get("/getcourse/{course_id}",response_model=schemas.course) 
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return db_course
 
@app.get('/getteacher/{teacher_id}', response_model=schemas.teacher)
def read_teacher(teacher_id:int,db:Session=Depends(get_db)):
    db_teacher=crud.get_teacher(teacher_id=teacher_id,db=db)
    if db_teacher is None:
        raise HTTPException(status_code=404,detail='teacher is not found')
    return db_teacher

@app.get( '/getteacher/{student_id}', response_model=schemas.student)
def read_student(student_id:int ,db:Session=Depends(get_db)):
    db_student=crud.get_student(db=db,student_id=student_id)
    if read_student is None:
        raise HTTPException(status_code=404, detail="student not found")
    return db_student
    
