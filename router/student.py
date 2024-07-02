from fastapi import Depends, HTTPException,Body
from sqlalchemy.orm import Session
from dependencies import get_db
import crud, schemas
from fastapi import APIRouter
import validation


router=APIRouter()

@router.post("/createstudent/", response_model=schemas.student)
def create_student(student:schemas.student,db:Session=Depends(get_db)):
    validation.checkstudent(value=student,db=db)
    db_student=crud.get_student(db=db,student_id=student.STID)
    if db_student:
        raise HTTPException(status_code=400,detail='دانشجو وجود دارد')
    return crud.create_student(db=db,student=student) 


@router.get( '/getstudent/{student_id}', response_model=schemas.student)
def read_student(student_id:int ,db:Session=Depends(get_db)):
    db_student=crud.get_student(db=db,student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="دانشجو یافت نشد")
    return db_student


@router.put("/updatestudent/{id}")
def update_student(student:schemas.student,id:int,db:Session=Depends(get_db)):
    db_student=crud.get_student(db=db,student_id=id)
    if db_student is None:
        raise HTTPException(status_code=400,detail="دانشجو یافت نشد")
    if student.STID!=id:
        db_student=crud.get_student(db=db,student_id=student.STID)
        if db_student:
            raise HTTPException(status_code=400,detail="دانشجو تکراری است ")
    validation.checkstudent(student)
    crud.update_student(db=db,data=student,id=id,)
    return "به روز رسانی اطلاعات دانشجو موفقیت امیز بود"


@router.delete("/deletestudent/{id}")
def delete_student(id:int,db:Session=Depends(get_db)):
    db_student=crud.get_student(db=db,student_id=id)
    if db_student is None:
        raise HTTPException(status_code=400,detail="دانشجو یافت نشد")
    crud.delete_student(db=db,id=id)
    return "دانشجو حذف شد"