from sqlalchemy import  Column, Integer, String,SMALLINT,ForeignKey
from database import Base

class course(Base):
    __tablename__='course'
    CID=Column(String,primary_key=True)
    CName=Column(String)
    Department=Column(String)
    Credit=Column(SMALLINT)

class teacher(Base):
    __tablename__='teacher'
    LID=Column(String,primary_key=True)
    FName=Column(String)
    LName=Column(String)
    ID=Column(String,unique=True)
    Department=Column(String)
    Major=Column(String)
    Birth=Column(String)
    Borncity=Column(String)
    Address=Column(String)
    Postalcode=Column(String)
    CPone=Column(String)
    HPone=Column(String)
    LCourseID=Column(String)

class student(Base):
    __tablename__='student'
    STID=Column(String,primary_key=True)
    FName=Column(String)
    LName=Column(String)
    Father=Column(String)
    Birth=Column(String)
    IDS=Column(String,unique=True)
    Borncity=Column(String)
    Address=Column(String)
    Postalcode=Column(String)
    CPone=Column(String)
    CHome=Column(String)
    Department=Column(String)
    Major=Column(String)
    Married=Column(String)
    ID=Column(String,unique=True)
    SCourse=Column(String)
    LIDs=Column(String)

class course_teacher_student(Base):
    __tablename__='course_teacher_tudent'
    counter=Column(Integer,primary_key=True)
    CID=Column(String,ForeignKey('course.CID'))
    LID=Column(String,ForeignKey('teacher.LID'))
    STID=Column(String,ForeignKey('student.STID'))
