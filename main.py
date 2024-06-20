from fastapi import FastAPI
import  models
from database import engine
from router import course, student, teacher

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(course.router)
app.include_router(teacher.router)
app.include_router(student.router) 
