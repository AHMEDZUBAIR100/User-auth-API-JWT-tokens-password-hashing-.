from fastapi import APIRouter, HTTPException

from database import users
from schemas import UserCreate
from security import password_hash


router = APIRouter()


@router.post("/register")
def register(user: UserCreate):

    for existing_user in users:

        if existing_user["username"] == user.username:
            raise HTTPException(
                status_code=400,
                detail="Username already exists"
            )

        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

    hashed_password = password_hash.hash(user.password)

    new_user = {
        "id": len(users) + 1,
        "username": user.username,
        "email": user.email,
        "password_hash": hashed_password
    }

    users.append(new_user)

    return {
        "message": "User registered successfully",
        "user": {
            "id": new_user["id"],
            "username": new_user["username"],
            "email": new_user["email"]
        }
    }