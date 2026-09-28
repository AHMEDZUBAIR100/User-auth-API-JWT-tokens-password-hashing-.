from fastapi import FastAPI

from routers.register import router as register_router
from routers.login import router as login_router
from routers.me import router as me_router

app = FastAPI()

app.include_router(register_router)
app.include_router(login_router)
app.include_router(me_router)


@app.get("/")
def home():
    return {"message": "Authentication API"}