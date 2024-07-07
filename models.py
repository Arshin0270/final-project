from sqlalchemy import  Column, Integer, String,SMALLINT,ForeignKey,Table
from database import Base
from sqlalchemy.orm import relationship



association_course_teacher=Table("association_course_teacher",Base.metadata,
    Column("CID",ForeignKey("course.CID",ondelete="cascade",onupdate="cascade")),
    Column("LID",ForeignKey("teacher.LID",ondelete="cascade",onupdate="cascade")))



association_course_student=Table("association_course_student",Base.metadata,
    Column("CID",ForeignKey("course.CID",ondelete="cascade",onupdate="cascade")),
    Column("STID",ForeignKey("student.STID",ondelete="cascade",onupdate="cascade")))




class course(Base):
    __tablename__='course'
    CID=Column(String,primary_key=True)
    CName=Column(String)
    Department=Column(String)
    Credit=Column(SMALLINT)
    students=relationship('student',secondary=association_course_student,back_populates='courses')
    teachers=relationship('teacher',secondary=association_course_teacher,back_populates='courses')

class teacher(Base):
    __tablename__='teacher'
    LID=Column(String,primary_key=True)
    FName=Column(String)
    LName=Column(String)
    ID=Column(String)
    Department=Column(String)
    Major=Column(String)
    Birth=Column(String)
    Borncity=Column(String)
    Address=Column(String)
    Postalcode=Column(String)
    CPone=Column(String)
    HPone=Column(String)
    courses=relationship('course',secondary=association_course_teacher,back_populates='teachers')

class student(Base):
    __tablename__='student'
    STID=Column(String,primary_key=True)
    FName=Column(String)
    LName=Column(String)
    Father=Column(String)
    Birth=Column(String)
    IDS=Column(String)
    Borncity=Column(String)
    Address=Column(String)
    Postalcode=Column(String)
    CPone=Column(String)
    CHome=Column(String)
    Department=Column(String)
    Major=Column(String)
    Married=Column(String)
    ID=Column(String)
    courses=relationship('course',secondary=association_course_student,back_populates='students')

