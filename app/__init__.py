from .models import FromForm
from .database import db
from .payment import Payment

from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
import os
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


def format_msg(msg):
    document = dict()
    msg_dict = msg.dict()
    document["name"] = msg_dict["name"]
    document["wpp"] = msg_dict["wpp"]
    document["msg"] = msg_dict["msg"]
    document["price"] = msg_dict["price"]
    document["paid"] = False
    return document


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
        document = format_msg(msg)
        payment = Payment(document)
        if payment.status == 201:
            document["payment_id"] = payment.pay_id
            document["payment_url"] = payment.url
            db.msg.insert_one(document.copy())
            return document
        else:
            response.status_code = payment.status
            return {"error": "Mercado Pago Error"}

    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"error": "Captcha Error"}
