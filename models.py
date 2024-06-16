from sqlalchemy import  Column, Integer, String,Boolean,BIGINT,SMALLINT,ForeignKey
from database import Base

class course(Base):
    __tablename__='course'
    CID=Column(Integer,primary_key=True)
    CName=Column(String)
    Department=Column(String)
    Credit=Column(SMALLINT)

class teacher(Base):
    __tablename__='teacher'
    LID=Column(Integer,primary_key=True)
    FName=Column(String)
    LName=Column(String)
    ID=Column(BIGINT,unique=True)
    Department=Column(String)
    Major=Column(String)
    Birth=Column(String)
    Borncity=Column(String)
    Address=Column(String)
    Postalcode=Column(BIGINT)
    CPone=Column(BIGINT)
    HPone=Column(BIGINT)
    LCourseID=Column(Integer)

class student(Base):
    __tablename__='student'
    STID=Column(BIGINT,primary_key=True)
    FName=Column(String)
    LName=Column(String)
    Father=Column(String)
    Birth=Column(String)
    IDS=Column(String,unique=True)
    Borncity=Column(String)
    Address=Column(String)
    Postalcode=Column(BIGINT)
    CPone=Column(BIGINT)
    CHome=Column(BIGINT)
    Department=Column(String)
    Major=Column(String)
    Married=Column(Boolean)
    ID=Column(BIGINT,unique=True)
    SCourse=Column(Integer)
    LIDs=Column(Integer)

class course_teacher_student(Base):
    __tablename__='course_teachero_tudent'
    counter=Column(Integer,primary_key=True)
    CID=Column(Integer,ForeignKey('course.CID'))
    LCourseID=Column(Integer,ForeignKey('teacher.LID'))
    LIDs=Column(Integer,ForeignKey('student.STID'))

