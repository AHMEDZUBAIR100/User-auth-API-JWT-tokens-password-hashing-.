from fastapi import APIRouter, Depends

from security import get_current_user


router = APIRouter()


@router.get("/me")
def get_me(current_user: dict = Depends(get_current_user)):

    return {
        "id": current_user["id"],
        "username": current_user["username"],
        "email": current_user["email"]
    }