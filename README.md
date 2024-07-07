


به نام خدا

گزارش پروژه پایانی

ارشین حسن زاده
 
First step:

در مرحله اول یک پگیج به اسم
 sql_app
میسازیم و ماژول های زیر را در ان ایجاد میکنیم


init.py
Schemas.py
Database.py
Router
Main.py
Models.py
Validation.py
Crud.py
.gitignore
Dockerfile
dependencies.py
 
__init__.py
 

این ماژول خالی است و برای تشکیل یک پکیج ایجاد میشود
.gitignore
 
هنگام کار با پایتون یک سری فایل به صورت پیش فرض با ران گرفتن از کد ایجاد میشوند برای اینکه این فایل ها از دید گیت پنهان بماند و گیت انهارا نادیده بگیرد از این ماژول استفاده میکنیم.
برای ساخت این ماژول میتوانیم از سایت 
Gitignore.io
با وارد کردن 
Venv و python
استفاده کنیم .بعد از وارد کردن این دومورد کل فایل متنی را کپی کرده و در ماژول کپی و سیو میکنیم.
 
database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 

در این ماژول ادرس دیتا بیس مشخص میشود 
در خط اول 
Create_engine 
را ایمپورت میکنیم و به کمک ان در خط هشتم 
Engine 
را میسازیم و ان را به ادرس دیتا بیس متصل میکنیم
در خط دوم 
Declaractive_base 
را ایمپورت میکنیم و در خط یازدهم از ان یک شی میسازیم 
تمام کلاس هایی که این شی را به ارث ببرند در ادرس ذکر شده در دیتا بیس به عنوان یک جدول شناسایی میشوند 
در خط سوم 
Sessionmaker 
را ایمپورت میکنیم و به کمک موتور یک مسیر بین ادرس دیتا بیس و فست ای پی ای ایجاد میکنیم
و در در خط پنجم ادرس دیتا بیس را مینویسیم
 
Models.py

class course(Base):
    __tablename__='course'
    CID=Column(String,primary_key=True)
    CName=Column(String)
    Department=Column(String)
    Credit=Column(SMALLINT)
    students=relationship('student',secondary=association_course_student,back_populates='courses')
    teachers=relationship('teacher',secondary=association_course_teacher,back_populates='courses')


این ماژول محل ساختن جداول دیتا بیس است
در این ماژول یک سری کلاس ایجاد میشوند که همگی 
Base(obj of declaractive_base)
را به ارث میبرند دارای نام و ستون هستند 
هر خط از این جدول یک ستون را در جدول دیتا بیس تشکیل میشود
در خط اول به کمک 
tablename
نام جدول را مشخص میکنیم
بعد از ان ستون های جدول را به کمک 
Column
ایجاد و نوع پارامتر ورودی به ان را داخل پرانتز مشخص میکنیم
هر جدول دارای یک ایتم به عنوان 
Primary_key 
است و رکورد های هر جدول به کمک این ایتم از رکورد شمارش میشوند
 
    
برای اینکه بتوانیم جدول ها را متصل کنیم و مقادیر مد نظر را چک کنیم لازم است دو جدول بسازیم که جدول درس هارا به دانشجو و بار دیگر با استاد متصل کند برای اینکار از کلاس
Table
یک 
Obj 
میسازیم 
ستون های مد نظرمان را میسازیم 
برای اینکه هنگام 
Updqte and delete 
داده ها به مشکل نخوریم از 
Cascade 
استفاده میکنیم
برای شناسایی این رابطه لازم است که در هر سه جدول 
Relationship
تعریف شود




association_course_teacher=Table("association_course_teacher",Base.metadata,
    Column("CID",ForeignKey("course.CID",ondelete="cascade",onupdate="cascade")),
    Column("LID",ForeignKey("teacher.LID",ondelete="cascade",onupdate="cascade")))


association_course_student=Table("association_course_student",Base.metadata,
    Column("CID",ForeignKey("course.CID",ondelete="cascade",onupdate="cascade")),
    Column("STID",ForeignKey("student.STID",ondelete="cascade",onupdate="cascade")))




Relationships:
Course:
  students=relationship('student',secondary=association_course_student,back_populates='courses')
    teachers=relationship('teacher',secondary=association_course_teacher,back_populates='courses')


student:
courses=relationship('course',secondary=association_course_student,back_populates='students')
teacher:
  courses=relationship('course',secondary=association_course_teacher,back_populates='teachers')

Schsmas.py
 
class course(BaseModel):
    CID:str
    CName:str
    Department:str
    Credit:int



در این ماژول نوع دیتا های ورودی بررسی میشود 
تمام کلاس ها در این ماژول از 
Basemodel 
ارث بری میکنند

 
         
Crud.py

در این ماژول توابعی برای ساخت جداول حذف اپدیت کردن و خواندن اطلاعات برای هر سه جدول مورد نظر ساخته شده است

from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy import update,delete
from fastapi import HTTPException

def get_course(db: Session, course_id: int):
    return db.query(models.course).filter(models.course.CID == course_id).first()


در توابع 
Get_/course/student/teacher
دو ارگومان ورودی باید ارسال شود 
db and course_id/teacher_id/student/id
که به ترتیب از نوع 
Session and int
هستند
نحوه کار این تابع به این گونه است که 
query 
به جداول دیتا بیس ارسال میشود اطلاعات ان به وسیله ی 
filter
محدود به بخش هایی میشود که 
Id
 در جدول با 
id
 ارسال شده توسط کاربر برابر است
اما چونیکتاست ما با استفاده از
first
مانع جست و جوی بیشتر میان سایر
id
ها میشویم و این به ما در اجرای برنامه ای سبک تر و بهتر کمک 
میکند



def get_teacher(db:Session,teacher_id:int):
    return db.query(models.teacher).filter(models.teacher.LID==teacher_id).first()




def get_student(db:Session ,student_id:int):
    return db.query(models.student).filter(models.student.STID==student_id).first()
 
درتوابع 
Create_/course/teacher/student
دو ارگومان ورودی 
db and course
وجود دارد
که متغییر دوم یک مدل پایدانتاکی است که توسط کاربر ارسال میشود
با استفاده از یک متغیر به نام
db_course/student/teacher
فیلد های جدول را با بخش های مدل پایدانتیکی ارسال شده توسط کاربر مقدار دهی میکنیم
با استفاده از تابع
add
متغییر ساخته شده را در دیتا بیس اضافه میکنیم 
با استفاده از 
Commit
اطلاعات وارد شده را ثبت نهایی و درنهایت با استفاده از 
Refresh 
اطلاعا را تازه سازی و در نهایت متغییر ساخته شده را برمیگردانیم
def create_course(db: Session, course: schemas.course):
    db_course = models.course(CID=course.CID, CName=course.CName,Department=course.Department,Credit=course.Credit)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
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


در نهایت با ایجاد یکسری تغیرات توابع را طوری تنظیم میکنیم که هنگام تشکیل و ساخت جداول اصلی جداول رابط با مقادیر ارسال شده مقدار دهی شوند
در توابع
delete_/course/student/teacher
دو ارگومان ورودی 
db و id 
وجود دارد
ابتدا با وسلیه یک متغییر به نام 
query
و با استفاده از تابع 
delete
وارد جدول موزد نظر میشویم با استفاده از 
Where 
اطلاعات جدول را به بخشی که 
Id 
جدول
با 
Id 
وارد شده یکسان است محدود میکند و درنهایت انرا حذف میکند 
با استفاده از 
Execute 
متغییر ساخته شده اجرا میشود
ود نهایت با استفاده از 
Commit 
تغییرات ثبت نهایی میشود

def delete_course(db:Session,id:int):
    delete1=models.association_course_student.delete().where(models.association_course_student.c.CID==id)
    delete2=models.association_course_teacher.delete().where(models.association_course_teacher.c.CID==id)
    query=delete(models.course).where(models.course.CID==id)
    db.execute(delete1)
    db.execute(delete2)
    db.execute(query)
    db.commit()


def delete_teacher(db:Session,id:int):
    delete1=models.association_course_teacher.delete().where(models.association_course_teacher.c.LID==id)
    query=delete(models.teacher).where(models.teacher.LID==id)
    db.execute(delete1)
    db.execute(query)
    db.commit()
def delete_student(db:Session,id:int):
    delete1=models.association_course_student.delete().where(models.association_course_student.c.STID==id)
    query=delete(models.student).where(models.student.STID==id)
    db.execute(delete1)
    db.execute(query)
    db.commit()

در نهایت با ایجاد یکسری تغییرات توابع را به گونه ای تنظیم میکنیم که در صورت حذف هر یک مقادیر در جداول اصل جدول رابط نیز تغییر کند و مقادیر و رکورد ها در جدول حذف شوند
در توابع 
Update_course/student/teacher
سه ارگومان وجود دارد
Id and data and db
در این تابع متغییری به نام 
Query 
ساخته میشود که در ان به کمک تابع 
Update 
وارد جدول مورد نظر شده و در جایی که 
Id 
وارد شده توسط کاربر با 
Id 
جدول یکسان است اطلاعت با 
Data 
اپدیت میشوند 
چون دیتای وارد شده توسط کاربر به صورت دیکشنری است و ودر جدول مقادیر به صورت مدل های پایدانتیکی مقدار دهی میشوند برای تطبیق این دو مدل متفاوت باهم از 
**data.dict()
استفاده میکنیم
در نهایت با استفاده از 
Execute 
متغییر را اجرا و با کمک 
Commit 
ان را ثبت نهایی میکنیم
def update_student(db:Session,data,id:int):
    delete1=models.association_course_student.update().where(models.association_course_student.c.STID==id).values(STID=data.STID)
    query=update(models.student).where(models.student.STID==id).values(ID=data.ID,STID=data.STID,FName=data.FName,LName=data.LName,Father=data.Father,Birth=data.Birth,IDS=data.IDS,Borncity=data.Borncity,Address=data.Address,Postalcode=data.Postalcode,CPone=data.CPone,CHome=data.CHome,Department=data.Department,Major=data.Major,Married=data.Married)
    db.execute(delete1)
    db.execute(query)
    db.commit()

def update_teacher(db:Session,teacher,id:int):
    delete1=models.association_course_teacher.update().where(models.association_course_teacher.c.LID==id).values(LID=teacher.LID)
    query=update(models.teacher).where(models.teacher.LID==id).values(LID=teacher.LID,FName=teacher.FName,LName=teacher.LName,ID=teacher.ID,Department=teacher.Department,Major=teacher.Major,Birth=teacher.Birth,Borncity=teacher.Borncity,Address=teacher.Address,Postalcode=teacher.Postalcode,CPone=teacher.CPone,HPone=teacher.HPone)
    db.execute(delete1)
    db.execute(query)
    db.commit()
def update_course(db:Session,data,id:int):
    
    student_u=models.association_course_student.update().where(models.association_course_student.c.CID==id).values(CID=data.CID)
    teacher_u=models.association_course_teacher.update().where(models.association_course_teacher.c.CID==id).values(CID=data.CID)
    query=update(models.course).where(models.course.CID==id).values(**data.dict())
    db.execute(student_u)
    db.execute(teacher_u)
    db.execute(query)
    db.commit()


در نهایت با ایجاد تغییراتی در تابع 
توابع را به گونه ای تنظیم میکنیم که در صورت هر گونه ایجاد اپدیت در جداول اصلی جداول رابطه نیز اپدیت شوند و مقادیر در انها تغییر کند
Dependencies.py

در این ماژول تنها یک تابع وجود دارد که تمام 
db 
ها به ان بستگی دارند و وابسته هستند
در این تابع ابتدا یک متغییر به نام 
db 
ساخته میشود یک 
Session 
است
هنگام اجرا شدن 
db 
رابرمیگرداند و در نهایت ان را میبندد




from database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()


Router

یک پکیج با نام 
Router
ایجاد میکنیم 
و ماژول های زیر را در ان ایجاد میکنیم
__init__.py
Student.py
Course.py
Teacher.py



course.py

ابتدا 
Apirouter 
را از 
Fastapi
ایمپورت میکنیم و از ان یک شی میسازیم


@router.post("/createcourse/", response_model=schemas.course)
def create_course(course: schemas.course, db: Session = Depends(get_db)):
    validation.checkcourse(value=course)
    db_course = crud.get_course(db=db,course_id=course.CID) 
    if db_course:
        raise HTTPException(status_code=400, detail="درس وجود دارد")
    return crud.create_course(db=db, course=course)


با استفاده از شی ساخته شده و به کمک متود 
Post 
یک 
URL
تعریف میکنیم و به کمک 
Response_model
از تابع میخواهیم که در پایان جدول ساخته شده را به کاربر برگرداند
تابعی تعریف میکنیم که در ان بتوانیم اطلاعات را در جدول ایجاد کنیم
این تابع دو ارگومان ورودی دارد
Course and db
که به ترتیب مدل پایدانتیکی و 
Session 
هستند
بعد از ان تابعی که برای اعتبار سنجی در 
ماژول 
Validation 
را فراخوانی میکنیم و مقدار ارگومان ورودی انرا با مدل پایدانتیکی ارسال شده توسط کاربر برابر قرار میدهیم
یک متغییر میسازیم و به کمک ان تابع 
Get_course
در ماژول 
Crud 
را فراخوانی میکنیم وارگومان های ورودی انرا با مقدار هایی که کاربر ارسال کرده برابر قرار میدهیم
این بخش از تابع بررسی میکند که ایا هیچ رکوردی از پیش با 
Id 
وارد شده در جدول موجود است یا خیر در صورت وجود ارور میدهد
در غیر این صورت تابع 
Create_course 
را ازهمان ماژول فرا خوانی میکند و ارگومان های ان را با مقادیر ارسال شده توسط کاربر برابر قرار میدهد و رکورد جدید میسازد
مراحل ذکر شده را در ماژول های 
Student and teacher 
برای جدول های دانشجو و استاد تکرار میکنیم
@router.get("/getcourse/{course_id}",response_model=schemas.course) 
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="درس یافت نشد")
    return db_course


با استفاده از شی ساخته شده با کمک متود 
Get 
یک 
URL
جدید تعریف میکنیم و در ان یک 
Id 
به عنوان 
Pathparameter
تعریف میکنیم و 
Response_model 
راهم مدل پایدانتیکی موجود در جدول قرار میدهیم
تابعی برای خواندن اطلاعات تعریف میکنیم کهدو ارگومان ورودی دارد 
Id and db
یک متغییر تعریف میکنیم به نام 
Db_course 
و به کمک ان تابع 
Get_course 
در ماژول 
Crud 
را فراخوانی میکنیم و ارگومان انرا با id ارسال شده به عنوان پارامتر مسیر برابر قرار میدهیم و اگر چیزی برنگرداند ارور برمیگردانیم 
این بخش از تابع به دنبال یک رکورد در جدول با 
Id
وارد شده توسط کاربر به عنوان پارامتر مسیر میگردد و در صورت عدم وجود ارور میدهد
در غیر این صورت تابع را مقدار دهی میکند و در متغییر قرار میدهد و انرا برمیگرداند

مراحل ذکر شده را در ماژول های 
Student and teacher 
برای جدول های دانشجو و استاد تکرار میکنیم

@router.delete("/deletecourse/{id}")
def delete_course(id:int,db:Session=Depends(get_db)):
    db_course=crud.get_course(db=db,course_id=id)
    if db_course is None:
        raise HTTPException(status_code=400,detail="درس یافت نشد")
    crud.delete_course(db=db,id=id)
    return "درس حذف شد"

با استفاده از شی ساخته شده و به کمک متود 
Delete
یک 
URL
جدید تعریف میکنیم و در ان 
Id
را به عنوان پارامتر مسیر در نظر میگیریم
یک تابع با نام
Update_course
برای به روز رسانی درس میسازیم و برای ان دو ارگومان ورودی 
id ,db 
در نظر میگیریم
یک متغیر به نام 
Get_db
تعریف میکنیم و در ان تابع 
Get_course 
را در ماژول 
Crud 
فراخوانی میکنیم و ارگومان های ورودی ان را با 
Id and db
ارسال شده مقدار دهی میکنیم این قسمت چک میکند که ایاهیچ رکوردی با ایدی وارد شده در جدول وجود دارد یا خیر اگر وجود نداشت ارور میدهد 
درغیر این صورت تابع 
Delete_course
را در ماژول 
Crud 
فراخوانی میکند و ارگومان های ورودی ان را با
Id and db 
ارسال شده مقدار دهی میکند و انرا حذف میکند 
سپس پیغام "درس حذف شد " را به کاربر برمیگرداند
مراحل قبل را در ماژول های 
Teacher , student
برای جداول دانشجو و استاد تکرار میکنیم
@router.put("/updatecourse/{id}")
def update_course(course: schemas.course,id:int ,db: Session = Depends(get_db)):
    db_course=crud.get_course(db=db,course_id=id )
    if db_course is None:
        raise HTTPException(status_code=400,detail="درس یافت نشد")
    if course.CID !=id :
        db_course=crud.get_course(db=db,course_id=course.CID )
        if db_course :
            raise HTTPException(status_code=400,detail="کد درس وارد شده تکراری است")       
    validation.checkcourse(course)
    crud.update_course(db=db,data=course,id=id)
    return "به روز رسانی درس موفقیت امیز بود"

با استفاده از شی ساخته شده و به کمک متود 
Put 
یک 
URL 
جدید تعریف میکنیم و به عنوان یک پارامتر مسیر 
Id 
را تعریف میکنیم
سپس یک تابع برای به روزرسانی اطلاعات تعریف میکنیم که سه ارگومان ورودی دارد 
Course and int and db
که 
Course 
در اینجا یک مدل پایدانتیکی است یک متغیر به نام
Get_db
تعریف میکنیم که در ان تابع 
Get_course 
در ماژول 
Crud 
فراخوانی میشود و ارگومان های ورودی ان مقدار دهی میشود
اگه این تابع مقدار 
None 
برگرداند و رکوردی با ایدی وارد شده به عنوان پارامتر مسیر پیدا نکرد ارور میدهد
در خط بعدی یک شرط جدید تعریف میکنیم که اگر 
Id 
وارد شده به عنوان پارامتر مسیر و 
Cid
در مدل پایدانتیکی ارسال شده برابر نبودند 
تابع قبلی در ماژول 
Crud 
دوباره فراخوانی میشود ولی اینبار به دنبال رکوردی میگردد که با 
Cid 
وارد شده 
Id 
یکسانی داشته باشد چرا که رکورد ها با این ایتم شمارش شده و باید یکتا باشند 
اگر موردی یافت شد به معنای تکراری بودن رکورد است درنتیجه باید ارور به کاربر نمایش داده شود 
در غیر این صورت مدل پایدانتیکی ارسال شده باید اعتبار سنجی شود 
اینکار با فراخوانی تابع 
Checkcourse
در ماژول 
Validation 
انجام میشود و ارگومان ورودی انرا با مدل پایدانتیکی ارسال شده برابر قرار میدهیم و انرا اعتبار سنجی میکنیم بعد از ان تابع 
Update_course 
در ماژول 
Crud 
را فراخوانی میکنیم و انرا مقدار دهی میکنیم سپش پیام "به روز رسانی درس موفقیت امیز بود "را به کاربر نمایش میدهیم
مراحل انجام شده را برای ماژول های 
Student and teacher
برای جداول دانشجو و استاد تکرار میکنیم
Validation.py
اعتبار سنجی مقادیر ارسال شده توسط کاربر در این ماژول انجام میشود
توابع استفاده شده در روتر ها را در این ماژول میسازیم و مقادیر ارسال شده برای سه جدول را به صورت جدا گانه در سه تابع مختلف 
Checkcourse
Checkstudent
Checkteacher
اعتبار سنجی میکنیم








Checkcourse:


def checkcourse(value):
    eror1={}
    if len(value.CID)!=5:
        eror1['CID']='کد درس باید یک عدد پنج رقمی باشد'
    if re.fullmatch(namepatern,value.CName)==None:
        eror1['CName']='نام درس فقط میتواند حاوی حروف فارسی باشد'
    if len(value.CName)>25:
        eror1['CName']='نام درس طولانی است'
    if  value.Department not in departments:
        eror1['Department']='دانشکده غیر مجاز است'
    if value.Credit>4 or value.Credit<1:
        eror1['Credit']='تعداد واحد درس نامعتبر است'
    if eror1!={}:
        raise HTTPException(detail=eror1,status_code=400)
    else:
        return value

ابتدا در هر تابع یک دیکشنری خالی تعریف میکنیم که در صورت بروز هر ارور ارور ها به صورت
Key_value
دیکشنری را پر کنند و در نهایت در صورت بروز ارور دیکشنری ساخته شده را به کاربر برمیگرداند
برای اعتبار سنجی نام درس ابتدا تعداد ارقام ان را با استفاده از تابع 
Len()
بررسی میکنیم و با یک شرط میخواهیم که تنها پنج رقم برای این ایتم ارسال شود در غیر این صورت دیکشنری ساخته شده با کلید و مقدار ذکر شده پر میشود
برا اعتبار سنجی نام درس از تابع 
Re.fullmatch()
استفاده میکنیم 
برای این کار لازم است یک پترن بسازیم که در ان تنها حروف فارسی قابل پذیرش باشند این تابع چک میکند که ایا مقدار ارسال شده با پترن کاملا هماهنگ هست یا خیر 
اگر خیر بود ارور با کلید و مقدار ذکر شده مقدار دهی میشود
برای ساخت پترن از 
Regular expression 
استفاده میکنیم

namepatern=r"^[آ-ی]+$"


با استفاده از تابع
Len()
تعداد حروف ارسال شده برای نام درس را محدود میکنیم
برای بررسی دانشکده ابتدا لازم است یک لیست از تمام دانکشده ها بسازیم سپس با استفاده از 
in
بررسی کنیم که ایا مقدار ارسال شده در لیست وجود دارد یا خیر
departments=['فنی و مهندسی','علوم پایه','علوم انسانی','دامپزشکی','اقتصاد','کشاورزی','منابع طبیعی']

در نهایت یک شرط میگذاریم که اگر دیکشنری خالی نبود 
یک ارور با 
Deatail
دیکشنری ساخته به کاربر نمایش دهد 
در غیر این صورت ارگومان ورودی را برگرداند







Checkteacher:
مشابه درس ابتدا یک دیکشنری خالی میسازیم
کد استاد ،نام،نام خانوادگی ،و دانشکده دقیقا مشابه به درس اعتبار سنجی میشوند
برای اعتبار سنجی رشته مشابه دانشکده یک لیست تعریف میکنیم و با استفاده از 
In 
چک میکنیم که ایا مقدار وارد شده در ان لیست موجود است یا خیر
اگر نبود دیکشنری را با کلید و مقدار مورد نظر از ارور دلخواه پر میکنیم
 
majors=["مهندسی عمران","مهندسی مکانیک","مهندسی برق","مهندسی کامپیوتر"مهندسی نرم‌افزار","مهندسی صنایع","مهندسی پزشکی","مهندسی هوافضا","مهندسی شیمی"]


برای اعتبار سنجی تاریخ تولد از 
Datetime
یک شی میسازیم و تابع
Srtptimr()
را فراخوانی میکنیم این تابع بررسی میکند که ایا تاریخ تولد وارد شده با الگوی وارد شده هماهنگ است یا خیر 
در غیر این صورت با استفاده از 
Try and except 
ارور میدهد
و در ان چک میکند که سال و ماه و روز وارد شده مقدار منطقی داشته باشند

مشابه رشته شهر وارد شده را به کمک یک لیست اعتبار سنجی میکنیم
به کمک تابع 
Len ()
ادرس وارد شده و طولانی بودن ان را بررسی میکنیمsss

 try:
        birthday=datetime.strptime(value.Birth,'%Y-%m-%d')
        if (birthday.year>1402) or (birthday.month>12 and birthday.month<1) or (birthday.day>30 and birthday.day<1):
            eror2['Birth']='تاریخ تولد اشتباه است'
    except ValueError:
        eror2['Birth']='تاریخ تولد اشتباه است'

با استفاده از توابع
Len()
طول شماره تلفن همراه و شماره تلفن منزل را بررسی میکنیم
با استفاده از تابع 
Startwith()
چک میکنیم که شماره های وارد شده با 
09 and 9
شروع شده باشند
با استفاده از 
Isdigit
چک میکنیم که برای شماره ها تنها عدد وارد شده باشد
 if len(value. Postalcode)!=10 or  value.Postalcode.isdigit()==False:
        eror2[' Postalcode']='کد پستی اشتباه است'
    if len(value.CPone)!=11 or  value.CPone.startswith('09')==False or value.CPone.isdigit()==False:
        eror2['CPone']='شماره تلفن نادرست است'
    if len(value.HPone)!=10 or  value.HPone.startswith('9')==False or value.HPone.isdigit()==False:
        eror2['HPone']='شماره تلفن ثابت نادرست است'


مشابه موارد قبلی برای اعتبار سنجی کد پستی از 
Len()and isdigit 
استفاده میکنیم و
برای کد ملی از 
Len()
استفاده میکنیم

به کمک یک متغیر و تابع 
Split 
از درس های اخذ شده توسط استاد یک لیست درست میکنیم
به کمک یک حلقه و تابع 
Get _course
چک میکنیم که درس اخذ شده توسط استاد در جدول درس ها موجود باشد در غیر این صورت ارور میدهد

Checkstudent:
تمام مقادیر در جدول دانشجو مانند جدول استاد اعتبار سنجی میشوند 
برای اعتبار سنجی کد دانشجو کافی است از ایندکس استفاده کنیم و با مقدار مورد نظر مقایسه کنیم اگر متفاوت بود ارور دهد
برای بررسی وضعیت تاهل دانشجو از یک لیست که دو عضو "مجرد"و"متاهل" 
دارد استفاده میکنیم اگر مقدار وارد شده در لیست نبود ارور میدهد

 
از درس های وارد شده یک لیست درست میکنیم به کمک 
Split
سپس به‌کمک 
Get_course 
چک میکنیم درس وارد شده در جدوا موجود باشد

 SCourse=value.SCourse.split("*")
    for i in SCourse:
        x=get_course(db=db,course_id=i)
        if x is None:
            raise HTTPException(status_code=400,detail="کد درس وارد شده در جدول موجود نیست")


Docerfile:
FROM   python:latest

WORKDIR /src


COPY ./requrements.txt/src


RUN pip install -r requrements.txt

COPY . .

CMD ["uvicorn","main.py:app","--host","8000"]


در نهایت ماژول داکر فایل را ایجاد میکنیم و در ان دستورات زیر را مینویسیم
این دستورات ابتدا 
Base image 
را نسخه 
Latest
از پایتون در نظر میگیرد 
سپس دایرکتوری ذکر شاده را میسازد و وارد ان میشود کل ماژول 
Requrement.txt 
را در دایرکتور کپی میکند 
این ماژول حاوی تمام نیازمندی های برنامه است
به کمک 
Run 
دستور ذکر شده را اجرا میکند
دیرکتوری فعلی را در دایرکتوری ساخته شده ذخیره میکند و در نهایت خط اخر اجرا میشود
