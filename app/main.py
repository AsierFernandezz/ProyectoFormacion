from fastapi import FastAPI
from app.routers import users
import app.routers.auth as auth
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(users.router, tags=["users"])
app.include_router(auth.router, tags=["auth"])