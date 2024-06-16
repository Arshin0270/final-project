from fastapi import FastAPI,HTTPException
from datetime import datetime
import re
namepatern=r"^[آ-ی]+$"
idsopatern=r"^\d{6}-\d{2}-[آ-ی]"
marriage=['مجرد','متاهل']
departments=['فنی و مهندسی','علوم پایه','علوم انسانی','دامپزشکی','اقتصاد','کشاورزی','منابع طبیعی']
majors=["مهندسی عمران","مهندسی مکانیک","مهندسی برق","مهندسی کامپیوتر","مهندسی نرم‌افزار","مهندسی صنایع","مهندسی پزشکی","مهندسی هوافضا","مهندسی شیمی"]

city=["تبریز","ارومیه","اردبیل","اصفهان", "کرج", "ایلام", "بوشهر",
     "تهران", "شهرکرد", "مشهد", "بیرجند", "بجنورد", "اهواز",
     "زنجان", "سمنان","زاهدان", "شیراز", "قزوین", "قم", "سنندج",
     "کرمان", "کرمانشاه", "یاسوج", "گرگان", "رشت", "خرم‌آباد", "ساری",
     "اراک", "بندرعباس", "یزد"]

def studentinfo():
    STID:int
    if len(STID)!=11:
        raise HTTPException(detail='شماره دانشجویی باید 11 رقم باشد',status_code=400)
    if STID[:3] not in (400-403):
        raise HTTPException(detail='بخش سال نادرست است',status_code=400)
    if STID[3:9]!=114151:
        raise HTTPException(detail='بخش ثابت نادرست است',status_code=400)
    Fname:str
    if len(Fname) not in(1-11):
        raise HTTPException(detail='نام باید حد اکثر 10 حرف باشد',status_code=400)
    elif re.fullmatch(Fname,namepatern)==None:
        raise HTTPException(detail='نام فقط حاوی حرو فارسی باشد'status_code=400)
    Lname:str
    if len(Lname) not in(1-11):
        raise HTTPException(detail='نام خانوادگی باید حد اکثر 10 حرف باشد',status_code=400)
    elif re.fullmatch(Lname,namepatern)==None:
        raise HTTPException(detail='نام فقط حاوی حرو فارسی باشد'status_code=400)
    Fathe=str
    if len(Fathe) not in(1-11):
        raise HTTPException(detail='نام پدر باید حد اکثر 10 حرف باشد',status_code=400)
    elif re.fullmatch(Fathe,namepatern)==None:
        raise HTTPException(detail='نام فقط حاوی حرو فارسی باشد'status_code=400)
    Birth=datetime()
    IDS=int
    if re.fullmatch(IDS,idsopatern)==None:
        raise HTTPException(detail='سریال شناسنمه اشتباه است'status_code=400)
    Borncity:str
    if Borncity not in city:
        raise HTTPException(detail='شهر وارد شده اشتباه است',status_code=400)
    Addres:str
    if len(Addres) not in (1-101):
        raise HTTPException(detail='ادرس طولانی است',status_code=400)
    Postalcode:int
    if len(Postalcode)!=10:
        raise HTTPException(detail='کد پستی باید ده رقم باشد',status_code=400)
    cphon:int
    Hphon:int
    Department:str
    if Department not in departments:
        raise HTTPException(detail='دانشکده اشتباه است',status_code=400)
    Major:str
    if Major not in majors:
        raise HTTPException(detail='رشته تحصیلی اشتباه است',status_code=400)
    Married:str
    if Married not in marriage:
        raise HTTPException(detail='',status_code=400)
    ID:int
    SCourseids:int
    LIDS:int



def teacherinfo():
    LID:int
    if len(LID)!=6:
        raise HTTPException(detail='',status_code=400)
    FName:str
    if len(FName) not in(1-11):
        raise HTTPException(detail='نام باید حد اکثر 10 حرف باشد',status_code=400)
    elif re.fullmatch(FName,namepatern)==None:
        raise HTTPException(detail='نام فقط حاوی حرو فارسی باشد'status_code=400)
    LName:str
    if len(LName) not in(1-11):
        raise HTTPException(detail='نام خانوادگی باید حد اکثر 10 حرف باشد',status_code=400)
    elif re.fullmatch(LName,namepatern)==None:
        raise HTTPException(detail='نام فقط حاوی حرو فارسی باشد'status_code=400)
    Department:str 
    if Department not in departments:
        raise HTTPException(detail='دانشکده اشتباه است',status_code=400)
    Major:str
    if Major not in majors:
        raise HTTPException(detail='رشته تحصیلی اشتباه است',status_code=400)
    Birth:
    Borncity:str
    if Borncity not in city:
        raise HTTPException(detail='شهر وارد شده اشتباه است',status_code=400)
    Address:str
    if len(Address) not in (0-101):
        raise HTTPException(detail='',status_code=400)
    postalcod:int
    if len(postalcod)!=6:
        raise HTTPException(detail='',status_code=400)
    cphon:int
    hphon:int
    LCourseID:int














app=FastAPI()
@app.post('/')
def checkinfo(student:studentinfo):
    return student




