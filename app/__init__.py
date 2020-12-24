from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"status": "OK"}


class Item(BaseModel):
    name: str
    wpp: str
    price: float
    msg: str


@app.post("/data/")
async def create_item(item: Item):
    return item