from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {'id':101, 'name':"Pratikcode", 'is_active':True}

user =User(**input_data)

print(user)