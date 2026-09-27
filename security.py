from pwdlib import PasswordHash
import jwt
from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from database import users


password_hash = PasswordHash.recommended()

SECRET_KEY = "my-super-secret-key"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def create_access_token(user_id: int):

    expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    payload = {
        "sub": str(user_id),
        "exp": expire
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def get_current_user(token: str = Depends(oauth2_scheme)):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = int(payload.get("sub"))

    except (jwt.InvalidTokenError, TypeError, ValueError):

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    for user in users:

        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=401,
        detail="User not found"
    )