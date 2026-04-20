from pydantic import BaseModel, field_validator, model_validator
from fastapi import FastAPI


add= FastAPI()

class User(BaseModel):
    username: str
    age: str
    passwd: str
    confirm_passwd: str

    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 charactes")
        return v
    
    @model_validator(mode="after")
    def checking_passwd(cls, self):
        if self.passwd != self.confirm_passwd:
            raise ValueError("Password do not match!!!")
        return self

