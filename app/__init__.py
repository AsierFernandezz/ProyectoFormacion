from fastapi import FastAPI

app = FastAPI(title="Mi API", version="0.1.0")
#init.py sirve para convertir la app en parquete
@app.get("/")
async def root():
    return {"message": "OK"}