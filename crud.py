from sqlalchemy.orm import Session
import models, schemas


def get_course(db: Session, course_id: int):
    return db.query(models.course).filter(models.course.CID == course_id).first()


def create_course(db: Session, course: schemas.course):
    db_course = models.course(CID=course.CID, CName=course.CName,Department=course.Department,Credit=course.Credit)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_teacher(db:Session,teacher_id:int):
    return db.query(models.teacher).filter(models.teacher.LID==teacher_id).first()

def create_teacher(db:Session,teacher:schemas.teacher):
    db_teacher=models.teacher(LID=teacher.LID,FName=teacher.FName,LName=teacher.LName,ID=teacher.ID,Department=teacher.Department,Major=teacher.Major,Birth=teacher.Birth,Borncity=teacher.Borncity,Address=teacher.Address,Postalcode=teacher.Postalcode,CPone=teacher.CPone,HPone=teacher.HPone,LCourseID=teacher.LCourseID)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def get_student(db:Session ,student_id:int):
    return db.query(models.student).filter(models.student.STID==student_id).first()

def create_student(db:Session,student:schemas.student):
    db_student=models.student(ID=student.ID,STID=student.STID,FName=student.FName,LName=student.LName,Father=student.Father,Birth=student.Birth,IDS=student.IDS,Borncity=student.Borncity,Address=student.Address,Postalcode=student.Postalcode,CPone=student.CPone,CHome=student.CHome,Department=student.Department,Major=student.Major,Married=student.Married,SCourse=student.SCourse,LIDs=student.LIDs)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student






