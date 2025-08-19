from fastapi import FastAPI
from app.api.v1 import api_v1_router

app = FastAPI(title="Getting Start")

@app.get("/")
def hello_world():
    return {"message" : "Hello World"}

app.include_router(api_v1_router)
