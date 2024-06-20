import re
from fastapi import HTTPException
from datetime import datetime



city=["تبریز","ارومیه","اردبیل","اصفهان", "کرج", "ایلام", "بوشهر",
     "تهران", "شهرکرد", "مشهد", "بیرجند", "بجنورد", "اهواز",
     "زنجان", "سمنان","زاهدان", "شیراز", "قزوین", "قم", "سنندج",
     "کرمان", "کرمانشاه", "یاسوج", "گرگان", "رشت", "خرم‌آباد", "ساری",
     "اراک", "بندرعباس", "یزد"]

eror={}
namepatern=r"^[آ-ی]+$"
idsopatern=r"^\d{6}-\d{2}-[آ-ی]"
departments=['فنی و مهندسی','علوم پایه','علوم انسانی','دامپزشکی','اقتصاد','کشاورزی','منابع طبیعی']
majors=["مهندسی عمران","مهندسی مکانیک","مهندسی برق","مهندسی کامپیوتر","مهندسی نرم‌افزار","مهندسی صنایع","مهندسی پزشکی","مهندسی هوافضا","مهندسی شیمی"]
marriage=['مجرد','متاهل']
def checkcourse(value):
    if len(value.CID)!=5:
        eror['CID']='کد درس باید یک عدد پنج رقمی باشد'
    if re.fullmatch(namepatern,value.CName)==None:
        eror['CName']='نام درس فقط میتواند حاوی حروف فارسی باشد'
    if len(value.CName)>25:
        eror['CName']='نام درس طولانی است'
    if  value.Department not in departments:
        eror['Department']='دانشکده غیر مجاز است'
    if value.Credit>4 or value.Credit<1:
        eror['Credit']='تعداد واحد درس نامعتبر است'



def checkteacher(value):
    if len(value.LID)!=6:
        eror['LID']='کد استاد نامعتبر است'
    if re.fullmatch(namepatern,value.FName)==None :
        eror['FName']='نام میتواند فقط حاوی حروف فارسی باشد '
    if len(value.Fname)>10:
        eror['FName']='نام وارد شده طولانی است'
    if re.fullmatch(namepatern,value.LName)==None:
       eror['LName']='نام خانوادگی میتواند فقط حاوی حروف فارسی باشد '
    if len(value.Lname)>10:
        eror['LName']='نام خانوادگی طولانی است'
    if  value.Department not in departments:
        eror['Department']='دانشکده غیر مجاز است'
    if  value.Major not in majors:
        eror['Major']='رشته غیر مجاز است'
    #birthday=datetime.strptime(value.Birth,'%Y-%m-%d')
    #if (birthday.year>1402) or (birthday.month>12 and birthday.month<1) or (birthday.day>30 and birthday.day<1):
       # eror['Birth']='تاریخ تولد اشتباه است'
    if  value.Borncity not in city:
        eror[' Borncity']='شهر وارد شده نا معتبر است'
    if len(value.Address)>100:
        eror['Address']='ادرس طولانی است'
    if len(value. Postalcode)!=10 or  value.Postalcode.isdigit()==False:
        eror[' Postalcode']='کد پستی اشتباه است'
    if len(value.CPone)!=11 or  value.CPone.startswith('09')==False or value.CPone.isdigit()==False:
        eror['CPone']='شماره تلفن نادرست است'
    if len(value.HPone)!=10 or  value.HPone.startswith('9')==False or value.HPone.isdigit()==False:
        eror['HPone']='شماره تلفن ثابت نادرست است'
    #ID,LCOURSEID
   
def checkstudent(value):
        
    if len(value.STID)!=11:
       eror['STID']='شماره دانشجویی باید 11 رقم باشد'
    if value.STID[:3]!=400 or value.STID[:3]!=401 or value.STID[:3]!=402 or value.STID[:3]!=403:
       eror['STID']='بخش سال نادرست است'
    if value.STID[3:9]!=114151:
       eror['STID']='بخش ثابت نادرست است'
    if len(value.FName)>10  :
        eror['FName']='نام باید حد اکثر 10 حرف باشد'
    elif re.fullmatch(value.Fname,namepatern)==None:
        eror['FName']='نام فقط حاوی حرو فارسی باشد'
    if len(value.LName)>10 :
        eror['LName']='نام خانوادگی باید حد اکثر 10 حرف باشد'
    elif re.fullmatch(value.Lname,namepatern)==None:
        eror['LName']='نام خانوادگی فقط حاوی حرو فارسی باشد'
    if len(value.Father)>10 :
        eror['Father']='نام پدر باید حد اکثر 10 حرف باشد'
    elif re.fullmatch(value.Father,namepatern)==None:
        eror['Father']='نام فقط حاوی حرو فارسی باشد'
    if re.fullmatch(value.IDS,idsopatern)==None:
        eror['IDS']='سریال شناسنمه اشتباه است'
    if value.Borncity not in city:
        eror[' Borncity']='شهر وارد شده اشتباه است'
    if len(value.Address)>100 :
        eror['Address']='ادرس طولانی است'
    if len(value.Postalcode)!=10 or  value.Postalcode.isdigit()==False:
        eror[' Postalcode']='کد پستی باید ده رقم باشد'
    if len(value.CPone)!=11 or  value.CPone.startswith('09')==False or value.CPone.isdigit()==False:
        eror['CPone']='شماره تلفن نادرست است'
    if len(value.CHome)!=10 or  value.CHome.startswith('9')==False or value.CHome.isdigit()==False:
        eror['CHome']='شماره تلفن ثابت نادرست است'
    if value.Department not in departments:
        eror['Department']='دانشکده اشتباه است'
    if value.Major not in majors:
        eror['Major']='رشته تحصیلی اشتباه است'
    if value.Married not in marriage:
        eror['Married ']='بخش وضعیت تاهل نادرس وارد شده است'
    #ID:int
    #SCourseids:int
    #LIDS:int
    #Birth





    if eror!={}:
        raise HTTPException(detail=eror,status_code=400)
    else:
        return value