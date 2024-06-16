from fastapi import FastAPI,HTTPException
from fastapi.params import Body
from datetime import datetime
import re

app=FastAPI()
@app.get('/')
def checknumbers(studentnumber:str):
    if len(studentnumber)!=11 or studentnumber.isdigit()==False:
        raise HTTPException(detail='شماره دانشجویی باید 11 رقم باشد',status_code=400)
    elif int(studentnumber[0:3]) not in range(400,403):
        raise HTTPException(detail='قسمت سال نادرست است',status_code=400)
    elif int(studentnumber[3:9]) !=114150:
        raise HTTPException(detail='قسمت ثابت نادرست است',status_code=400)
    elif int(studentnumber[9:]) not in range(1,100):
        raise HTTPException(detail=' قسمت اندیس نادرست',status_code=400)
    return f'{studentnumber}  شماره دانشجویی وارد شده درست است'


@app.get('/{studentnumber}')
def checknumbers(studentnumber:str):
    if len(studentnumber)!=11 or studentnumber.isdigit()==False:
        raise HTTPException(detail='شماره دانشجویی باید 11 رقم باشد',status_code=400)
    elif int(studentnumber[0:3]) not in range(400,403):
        raise HTTPException(detail='قسمت سال نادرست است',status_code=400)
    elif int(studentnumber[3:9]) !=114150:
        raise HTTPException(detail='قسمت ثابت نادرست است',status_code=400)
    elif int(studentnumber[9:]) not in range(1,100):
        raise HTTPException(detail=' قسمت اندیس نادرست',status_code=400)
    return f'{studentnumber}  شماره دانشجویی وارد شده درست است'
 



@app.post('/')
def checkinfo(student:dict = Body()):
    eror={}
    patern=r"^[آ-ی]+$"
    patern2=r"^\d{6}-\d{2}-[آ-ی]"
    ostan={"آذربایجان شرقی": "تبریز","آذربایجان غربی": "ارومیه","اردبیل": "اردبیل","اصفهان": "اصفهان","البرز": "کرج","ایلام": "ایلام","بوشهر": "بوشهر",
    "تهران": "تهران","چهارمحال و بختیاری": "شهرکرد","خراسان رضوی": "مشهد","خراسان جنوبی": "بیرجند","خراسان شمالی": "بجنورد","خوزستان": "اهواز",
    "زنجان": "زنجان","سمنان": "سمنان","سیستان و بلوچستان": "زاهدان","فارس": "شیراز","قزوین": "قزوین","قم": "قم","کردستان": "سنندج",
    "کرمان": "کرمان","کرمانشاه": "کرمانشاه","کهگیلویه و بویراحمد": "یاسوج","گلستان": "گرگان","گیلان": "رشت","لرستان": "خرم‌آباد","مازندران": "ساری",
    "مرکزی": "اراک","هرمزگان": "بندرعباس","همدان": "همدان","یزد": "یزد"}
    mariage=["متاهل","مجرد"]
    daneshkadeh=['فنی و مهندسی','علوم پایه','علوم انسانی','دامپزشکی','اقتصاد','کشاورزی','منابع طبیعی']
    reshteh=["مهندسی عمران","مهندسی مکانیک","مهندسی برق","مهندسی کامپیوتر","مهندسی نرم‌افزار","مهندسی صنایع",
                        "مهندسی پزشکی","مهندسی هوافضا","مهندسی شیمی"]
    birthday=datetime.strptime(student['birthday'],'%Y-%m-%d')


    if len(student['student-number'])!=11 or student['student-number'].isdigit()==False:
        eror['student-number']='شماره دانشجویی باید 11 رقم باشد'
    elif int(student['student-number'][0:3]) not in range(400,403):
        eror['student-number']='قسمت سال نادرست است'
    elif int(student['student-number'][3:9])!=114150:
        eror['student-number']='قسمت ثابت نادرست است'
    elif int(student['student-number'][9:]) not in range(0,100):
        eror['student-number']='قسمت اندیس نادرست است'



    if len(student['name'])>10 :
        eror['name']='حداکثر طول 10 می باشد'  
    elif re.fullmatch(patern,student['name'])==None:
        eror['name']="نام فقط حاوی حروف فارسی باشد"



    if (birthday.year>1402) or (birthday.month>12 and birthday.month<1) or (birthday.day>30 and birthday.day<1):
        eror['birthday']='تاریخ تولد اشتباه است'



    if re.match(patern2,student['id'])==None:
        eror['id']='سریال شناسنامه نامعتبر است'



    if ostan.get(student['ostan'])==None:
        eror['ostan']='استان نامعتبر است'
    elif ostan[student['ostan']]!=student['shahrestan']:
        eror['ostan or shahrestan']='استان و یا شهرستان نامعتبر است'




    if len(student['address'])>100 or re.fullmatch(patern,student['address'])==None:
        eror['address']='آدرس نامعتبر است'



    if len(student['post-code'])!=10 or student['post-code'].isdigit()==False:
        eror['post-code']='کد پستی نامعتبر است'



    if student['mariage'] not in mariage:
        eror['mariage']='وضعیت تعهل نامعتبر'



    if student['daneshkadeh'] not in daneshkadeh:
        eror['daneshkadeh']='دانشکده نامعتبر است'



    if student['reshteh'] not in reshteh:
        eror['reshteh']='رشته نا معتبر است'



    if len(student['phone-number'])!=11 or  student['phone-number'].startswith('09')==False or student['phone-number'].isdigit()==False:
        eror['phone-number']='شماره تلفن نادرست است'
    


    if len(student['home-number'])!=10 or int(student['home-number'][0])!=9 or student['home-number'].isdigit()==False:
        eror['home-number']='شماره ثابت نادرست است'


    if len(student['code-melli'])!=10 or student['code-melli'].isdigit()==False:
        eror['code-melli']='کد ملی نامعتبر است'




    if eror!={}:
        raise HTTPException(detail=eror,status_code=400)
    else:
        return student
        



