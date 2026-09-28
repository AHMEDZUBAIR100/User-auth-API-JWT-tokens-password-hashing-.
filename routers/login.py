from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from database import users
from security import password_hash, create_access_token


router = APIRouter()


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    for stored_user in users:

        if stored_user["username"] == form_data.username:

            if password_hash.verify(
                form_data.password,
                stored_user["password_hash"]
            ):

                token = create_access_token(
                    stored_user["id"]
                )

                return {
                    "access_token": token,
                    "token_type": "bearer"
                }

            raise HTTPException(
                status_code=401,
                detail="Incorrect password"
            )

    raise HTTPException(
        status_code=401,
        detail="User not found"
    )