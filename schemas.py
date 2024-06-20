from pydantic import BaseModel




class course(BaseModel):
    CID:str
    CName:str
    Department:str
    Credit:int

class teacher(BaseModel):
    LID:str
    FName:str
    LName:str
    ID:int
    Department:str
    Major:str
    Birth:str
    Borncity:str
    Address:str
    Postalcode:str
    CPone:str
    HPone:str
    LCourseID:str

class student(BaseModel):
    STID:str
    FName:str
    LName:str
    Father:str
    Birth:str
    IDS:str
    Borncity:str
    Address:str
    Postalcode:str
    CPone:str
    CHome:str
    Department:str
    Major:str
    Married:str
    ID:int
    SCourse:str
    LIDs:str


