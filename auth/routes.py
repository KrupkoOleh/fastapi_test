from typing import Annotated

from fastapi import HTTPException, APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from auth.crud import (fake_users_db, get_user,
                       fake_hash_password, get_current_active_user)

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = get_user(fake_users_db, form_data.username)
    if not user:
        raise HTTPException(status_code=400,
                            detail="Incorrect username or password")
    hashed_password = fake_hash_password(form_data.password)
    if hashed_password != user["hashed_password"]:
        raise HTTPException(status_code=400,
                            detail="Incorrect username or password")

    return {"access_token": user['username'], "token_type": "bearer"}


@router.get("/user-info-secure")
async def secure_data(user: dict = Depends(get_current_active_user)):
    return {"msg": "Secure info", "user": user}
