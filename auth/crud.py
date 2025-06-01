from typing import Annotated

from fastapi import HTTPException, Depends, APIRouter, status
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

fake_users_db = {
    "olegk": {
        "username": "olegk",
        "hashed_password": "fakehashedpassword",
        "disabled": False,
    }
}


def fake_hash_password(password: str):
    return "fakehashed" + password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def get_user(db, username: str):
    if username not in db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User not found')
    return db.get(username)


def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(
    current_user: Annotated[dict, Depends(get_current_user)],
):
    if current_user.get('disabled'):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
