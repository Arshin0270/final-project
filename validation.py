import re
from fastapi import HTTPException
from datetime import datetime



city=["تبریز","ارومیه","اردبیل","اصفهان", "کرج", "ایلام", "بوشهر","تهران", "شهرکرد", "مشهد", "بیرجند", "بجنورد", "اهواز","زنجان", "سمنان","زاهدان", "شیراز", "قزوین", "قم", "سنندج","کرمان", "کرمانشاه", "یاسوج", "گرگان", "رشت", "خرم‌آباد", "ساری","اراک", "بندرعباس", "یزد"]


namepatern=r"^[آ-ی]+$"
idsopatern=r"^\d{6}-\d{2}-[آ-ی]"
departments=['فنی و مهندسی','علوم پایه','علوم انسانی','دامپزشکی','اقتصاد','کشاورزی','منابع طبیعی']
majors=["مهندسی عمران","مهندسی مکانیک","مهندسی برق","مهندسی کامپیوتر","مهندسی نرم‌افزار","مهندسی صنایع","مهندسی پزشکی","مهندسی هوافضا","مهندسی شیمی"]
marriage=['مجرد','متاهل']



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





 

def checkteacher(value):
    eror2={}
    if len(value.LID)!=6:
        eror2['LID']='کد استاد نامعتبر است'
    if re.fullmatch(namepatern,value.FName)==None :
        eror2['FName']='نام میتواند فقط حاوی حروف فارسی باشد '
    if len(value.FName)>10:
        eror2['FName']='نام وارد شده طولانی است'
    if re.fullmatch(namepatern,value.LName)==None:
       eror2['LName']='نام خانوادگی میتواند فقط حاوی حروف فارسی باشد '
    if len(value.LName)>10:
        eror2['LName']='نام خانوادگی طولانی است'
    if  value.Department not in departments:
        eror2['Department']='دانشکده غیر مجاز است'
    if  value.Major not in majors:
        eror2['Major']='رشته غیر مجاز است'
    try:
        birthday=datetime.strptime(value.Birth,'%Y-%m-%d')
        if (birthday.year>1402) or (birthday.month>12 and birthday.month<1) or (birthday.day>30 and birthday.day<1):
            eror2['Birth']='تاریخ تولد اشتباه است'
    except ValueError:
        eror2['Birth']='تاریخ تولد اشتباه است'
    if  value.Borncity not in city:
        eror2[' Borncity']='شهر وارد شده نا معتبر است'
    if len(value.Address)>100:
        eror2['Address']='ادرس طولانی است'
    if len(value. Postalcode)!=10 or  value.Postalcode.isdigit()==False:
        eror2[' Postalcode']='کد پستی اشتباه است'
    if len(value.CPone)!=11 or  value.CPone.startswith('09')==False or value.CPone.isdigit()==False:
        eror2['CPone']='شماره تلفن نادرست است'
    if len(value.HPone)!=10 or  value.HPone.startswith('9')==False or value.HPone.isdigit()==False:
        eror2['HPone']='شماره تلفن ثابت نادرست است'
    if len(value.ID)!=10:
        eror2['ID']='کد ملی نامعتبر است'
    if eror2!={}:
        raise HTTPException(detail=eror2,status_code=400)
    else:
        return value






   
def checkstudent(value):
    eror3={}
    if len(value.STID)!=11:
       eror3['STID']='شماره دانشجویی باید 11 رقم باشد'
    elif value.STID[0:3] not in ['400','401','402']:
       eror3['STID']='بخش سال نادرست است'
    elif value.STID[3:9]!='114150':
       eror3['STID']='بخش ثابت نادرست است'
    if len(value.FName)>10  :
        eror3['FName']='نام باید حد اکثر 10 حرف باشد'
    elif re.fullmatch(namepatern,value.FName)==None:
        eror3['FName']='نام فقط حاوی حروف فارسی باشد'
    if len(value.LName)>10 :
        eror3['LName']='نام خانوادگی باید حد اکثر 10 حرف باشد'
    elif re.fullmatch(namepatern,value.LName)==None:
        eror3['LName']='نام خانوادگی فقط حاوی حروف فارسی باشد'
    if len(value.Father)>10 :
        eror3['Father']='نام پدر باید حد اکثر 10 حرف باشد'
    elif re.fullmatch(namepatern,value.Father)==None:
        eror3['Father']='نام فقط حاوی حروف فارسی باشد'
    if re.fullmatch(idsopatern,value.IDS)==None:
        eror3['IDS']='سریال شناسنامه اشتباه است'
    if value.Borncity not in city:
        eror3[' Borncity']='شهر وارد شده اشتباه است'
    if len(value.Address)>100 :
        eror3['Address']='ادرس طولانی است'
    if len(value.Postalcode)!=10 or  value.Postalcode.isdigit()==False:
        eror3[' Postalcode']='کد پستی باید ده رقم باشد'
    if len(value.CPone)!=11 or  value.CPone.startswith('09')==False or value.CPone.isdigit()==False:
        eror3['CPone']='شماره تلفن نادرست است'
    if len(value.CHome)!=10 or  value.CHome.startswith('9')==False or value.CHome.isdigit()==False:
        eror3['CHome']='شماره تلفن ثابت نادرست است'
    if value.Department not in departments:
        eror3['Department']='دانشکده اشتباه است'
    if value.Major not in majors:
        eror3['Major']='رشته تحصیلی اشتباه است'
    if value.Married not in marriage:
        eror3['Married ']='بخش وضعیت تاهل نادرس وارد شده است'
    try :
        birthday=datetime.strptime(value.Birth,'%Y-%m-%d')
        if (birthday.year>1402) or (birthday.month>12 and birthday.month<1) or (birthday.day>30 and birthday.day<1):
            eror3['Birth']='تاریخ تولد اشتباه است'
    except ValueError:
        eror3['Birth']='تاریخ تولد اشتباه است'
    if len(value.ID)!=10:
        eror3['ID']='کد ملی نامعتبر است'
    if eror3!={}:
        raise HTTPException(detail=eror3,status_code=400)
    else:
        return value





    