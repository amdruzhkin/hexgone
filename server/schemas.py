from pydantic import BaseModel

class UserInfo(BaseModel):
    login: str
    email: str

    class Config:
        orm_mode = True

class UserSignIn(BaseModel):
    login: str
    password: str

    class Config:
        orm_mode = True

class UserSignUp(BaseModel):
    login: str
    email: str
    password: str

    class Config:
        orm_mode = True