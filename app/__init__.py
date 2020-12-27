from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
import os
import requests

from .models import FromForm
from .database import db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*localhost.*",
    allow_origins=[
        "http://127.0.0.1:5500",
        "https://felipe-e-wendy.github.io/",
    ],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.on_event("shutdown")
async def disconnect():
    db.close()


@app.get("/")
async def read_root():
    return {"status": "OK"}


@app.post("/msg", status_code=200)
async def create_item(msg: FromForm, response: Response):
    SECRET_RECAPTCHAV2 = os.environ["SECRET_RECAPTCHAV2"]
    data = {"secret": SECRET_RECAPTCHAV2, "response": msg.token}
    response_captcha = requests.post(
        "https://www.google.com/recaptcha/api/siteverify", data=data
    ).json()

    if response_captcha["success"]:
        document = dict()
        msg_dict = msg.dict()
        document["name"] = msg_dict["name"]
        document["wpp"] = msg_dict["wpp"]
        document["msg"] = msg_dict["msg"]
        document["price"] = msg_dict["price"]
        document["payment_id"] = "test paid id"
        document["paid"] = False
        db.msg.insert_one(document.copy())
        return document

    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"error": "Captcha Error"}
