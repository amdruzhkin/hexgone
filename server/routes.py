from fastapi import APIRouter, Depends
from schemas import UserSignIn, UserSignUp, UserInfo
from typing import Union
from database import get_session
from services import *

auth_router = APIRouter()

@auth_router.post("/api/v1/sign_in")
async def sign_in(payload: UserSignIn):
    return {"status": "success"}

@auth_router.post("/api/v1/sign_up")
async def sign_up(payload: UserSignUp):
    return {"status": "success"}

@auth_router.get("/api/v1/user/{uid}", response_model=UserInfo)
async def user_info(uid: Union[int, str], session: Session = Depends(get_session)):
    if type(uid) == int:
        return await get_user_by_id(session, uid)
    elif type(uid) == str:
        return await get_user_by_login(session, uid)