from pydantic import BaseModel
from datetime import date



class course(BaseModel):
    CID:int
    CName:str
    Department:str
    Credit:int

class teacher(BaseModel):
    LID:int
    FName:str
    LName:str
    ID:int
    Department:str
    Major:str
    Birth:str
    Borncity:str
    Address:str
    Postalcode:int
    CPone:int
    HPone:int
    LCourseID:int

class student(BaseModel):
    STID:int
    FName:str
    LName:str
    Father:str
    Birth:str
    IDS:str
    Borncity:str
    Address:str
    Postalcode:int
    CPone:int
    CHome:int
    Department:str
    Major:str
    Married:bool
    ID:int
    SCourse:int
    LIDs:int


