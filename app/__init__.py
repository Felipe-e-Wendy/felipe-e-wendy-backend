from typing import Optional

from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"status": "OK"}


class Item(BaseModel):
    name: str
    wpp: str
    price: float
    msg: str
    token: str


@app.post("/data/", status_code=200)
async def create_item(item: Item, response: Response):
    SECRET_RECAPTCHAV2 = os.environ["SECRET_RECAPTCHAV2"]
    data = {"secret": SECRET_RECAPTCHAV2, "response": item.token}
    response_captcha = requests.post(
        "https://www.google.com/recaptcha/api/siteverify", data=data
    ).json()

    if response_captcha["success"]:
        return item
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return item
