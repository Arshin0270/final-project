from fastapi import Depends, HTTPException,Body
from sqlalchemy.orm import Session
from dependencies import get_db
import crud, schemas
from fastapi import APIRouter
import validation


router=APIRouter()


@router.post("/createteacher/", response_model=schemas.teacher)
def create_teacher(teacher:schemas.teacher,db:Session=Depends(get_db)):
    validation.checkteacher(value=teacher,db=db)
    db_teacher=crud.get_teacher(db=db,teacher_id=teacher.LID)
    if db_teacher!=None:
        raise HTTPException(status_code=400,detail='استاد وجود دارد')
    return crud.create_teacher(db=db,teacher=teacher)


@router.get('/getteacher/{teacher_id}', response_model=schemas.teacher)
def read_teacher(teacher_id:int,db:Session=Depends(get_db)):
    db_teacher=crud.get_teacher(teacher_id=teacher_id,db=db)
    if db_teacher is None:
        raise HTTPException(status_code=404,detail='استاد یافت نشد')
    return db_teacher

@router.put("/updateteacher/{id}")
def update_teacher(teacher:schemas.teacher,id:int,db:Session=Depends(get_db)):
    db_teacher=crud.get_teacher(db=db ,teacher_id=id)
    if db_teacher is None:
        raise HTTPException(status_code=400,detail="استاد یافت نشد")
    if teacher.LID!=id:
        db_teacher=crud.get_teacher(db=db ,teacher_id=teacher.LID)
        if db_teacher:
            raise HTTPException(status_code=400,detail=" استاد تکراری است")

    validation.checkteacher(teacher)
    crud.update_teacher(db=db,data=teacher,id=id)
    return  "به روز رسانی اطلاعات استاد موفقیت امیز بود"


@router.delete("/deleteteacher/{id}")
def delete_teacher(id:int,db:Session=Depends(get_db)):
    db_teacher=crud.get_teacher(db=db,teacher_id=id)
    if db_teacher is None:
        raise HTTPException(status_code=400,detail="استاد موجود نیست")
    crud.delete_teacher(db=db,id=id)
    return "حذف اطلاعات استاد مورد نظر موفقیت امیز بود"




