from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy import update,delete
from fastapi import HTTPException

def get_course(db: Session, course_id: int):
    return db.query(models.course).filter(models.course.CID == course_id).first()

def create_course(db: Session, course: schemas.course):
    db_course = models.course(CID=course.CID, CName=course.CName,Department=course.Department,Credit=course.Credit)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def update_course(db:Session,data,id:int):
    
    student_u=models.association_course_student.update().where(models.association_course_student.c.CID==id).values(CID=data.CID)
    teacher_u=models.association_course_teacher.update().where(models.association_course_teacher.c.CID==id).values(CID=data.CID)
    query=update(models.course).where(models.course.CID==id).values(**data.dict())
    db.execute(student_u)
    db.execute(teacher_u)
    db.execute(query)
    db.commit()

def delete_course(db:Session,id:int):
    delete1=models.association_course_student.delete().where(models.association_course_student.c.CID==id)
    delete2=models.association_course_teacher.delete().where(models.association_course_teacher.c.CID==id)
    query=delete(models.course).where(models.course.CID==id)
    db.execute(delete1)
    db.execute(delete2)
    db.execute(query)
    db.commit()


def get_teacher(db:Session,teacher_id:int):
    return db.query(models.teacher).filter(models.teacher.LID==teacher_id).first()

def create_teacher(db:Session,teacher:schemas.teacher):
    for i in teacher.LCourseID.split('*'):
        course=db.query(models.association_course_teacher).filter(models.association_course_teacher.c.CID==i).first()
        if course:
            raise HTTPException(status_code=400,detail='درس متعلق به استاد دیگری است')
    db_teacher=models.teacher(LID=teacher.LID,FName=teacher.FName,LName=teacher.LName,ID=teacher.ID,Department=teacher.Department,Major=teacher.Major,Birth=teacher.Birth,Borncity=teacher.Borncity,Address=teacher.Address,Postalcode=teacher.Postalcode,CPone=teacher.CPone,HPone=teacher.HPone)
    db.add(db_teacher)
    db.commit()
    teacher1=get_teacher(db=db,teacher_id=teacher.LID)
    for x in teacher.LCourseID.split('*'):
        course=get_course(db=db, course_id=x)
        course.teachers.append(teacher1)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def update_teacher(db:Session,teacher,id:int):
    delete1=models.association_course_teacher.update().where(models.association_course_teacher.c.LID==id).values(LID=teacher.LID)
    query=update(models.teacher).where(models.teacher.LID==id).values(LID=teacher.LID,FName=teacher.FName,LName=teacher.LName,ID=teacher.ID,Department=teacher.Department,Major=teacher.Major,Birth=teacher.Birth,Borncity=teacher.Borncity,Address=teacher.Address,Postalcode=teacher.Postalcode,CPone=teacher.CPone,HPone=teacher.HPone)
    db.execute(delete1)
    db.execute(query)
    db.commit()

def delete_teacher(db:Session,id:int):
    delete1=models.association_course_teacher.delete().where(models.association_course_teacher.c.LID==id)
    query=delete(models.teacher).where(models.teacher.LID==id)
    db.execute(delete1)
    db.execute(query)
    db.commit()

def get_student(db:Session ,student_id:int):
    return db.query(models.student).filter(models.student.STID==student_id).first()

def create_student(db:Session,student:schemas.student):

    db_student=models.student(ID=student.ID,STID=student.STID,FName=student.FName,LName=student.LName,Father=student.Father,Birth=student.Birth,IDS=student.IDS,Borncity=student.Borncity,Address=student.Address,Postalcode=student.Postalcode,CPone=student.CPone,CHome=student.CHome,Department=student.Department,Major=student.Major,Married=student.Married)
    db.add(db_student)
    db.commit()
    student1=get_student(db=db,student_id=student.STID)
    for x in student.SCourse.split('*'):
        course=get_course(db=db, course_id=x)
        course.students.append(student1)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db:Session,data,id:int):
    delete1=models.association_course_student.update().where(models.association_course_student.c.STID==id).values(STID=data.STID)
    query=update(models.student).where(models.student.STID==id).values(ID=data.ID,STID=data.STID,FName=data.FName,LName=data.LName,Father=data.Father,Birth=data.Birth,IDS=data.IDS,Borncity=data.Borncity,Address=data.Address,Postalcode=data.Postalcode,CPone=data.CPone,CHome=data.CHome,Department=data.Department,Major=data.Major,Married=data.Married)
    db.execute(delete1)
    db.execute(query)
    db.commit()

def delete_student(db:Session,id:int):
    delete1=models.association_course_student.delete().where(models.association_course_student.c.STID==id)
    query=delete(models.student).where(models.student.STID==id)
    db.execute(delete1)
    db.execute(query)
    db.commit()





