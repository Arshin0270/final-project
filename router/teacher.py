from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
import crud, schemas
from fastapi import APIRouter
import validation


router=APIRouter()


@router.post("/createteacher/", response_model=schemas.teacher)
def create_teacher(teacher:schemas.teacher,db:Session=Depends(get_db)):
    validation.checkteacher(value=teacher)
    db_teacher=crud.get_teacher(db=db,teacher_id=teacher.LID)
    if db_teacher!=None:
        raise HTTPException(status_code=400,detail='teacher already exists')
    return crud.create_teacher(db=db,teacher=teacher)


@router.get('/getteacher/{teacher_id}', response_model=schemas.teacher)
def read_teacher(teacher_id:int,db:Session=Depends(get_db)):
    db_teacher=crud.get_teacher(teacher_id=teacher_id,db=db)
    if db_teacher is None:
        raise HTTPException(status_code=404,detail='teacher is not found')
    return db_teacher