from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud, schemas
from fastapi import APIRouter
import validation


router=APIRouter()

@router.post("/createstudent/", response_model=schemas.student)
def create_student(student:schemas.student,db:Session=Depends(get_db)):
    validation.checkstudent(value=student)
    db_student=crud.get_student(db=db,student_id=student.STID)
    if db_student!=None:
        raise HTTPException(status_code=400,detail='student already exists')
    return crud.create_student(student=student,db=db) 


@router.get( '/getteacher/{student_id}', response_model=schemas.student)
def read_student(student_id:int ,db:Session=Depends(get_db)):
    db_student=crud.get_student(db=db,student_id=student_id)
    if read_student is None:
        raise HTTPException(status_code=404, detail="student not found")
    return db_student