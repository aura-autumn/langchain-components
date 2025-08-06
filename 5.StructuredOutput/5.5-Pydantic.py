from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'New student'
    age: Optional[int]=None
    email: EmailStr = "python@langchain.com"
    cgpa: float = Field(ge=0, le=10, default=0, description="Cummulative Grade Point Average")

new_std={'name':'Ray', 'age':"24", 'email':'Ray@langchain.com', 'cgpa':9.5}
std2=Student()

std1=Student(**new_std)
std3=dict(std2)
std4=std2.model_dump_json()

print(std1)
print(type(std1.age))
print(std2)
print(std3)
print(type(std3))
print(std4)
print(type(std4))