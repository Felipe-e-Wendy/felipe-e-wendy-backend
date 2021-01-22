import mercadopago
import json
from os import environ
import re


class Payment:
    pattern = re.compile("\d+")
    mp = mercadopago.MP(environ["MEPAGO_ACCESS_TOKEN"])

    def __init__(self, document: dict):
        numbers = Payment.pattern.findall(document["wpp"])
        codigo = numbers[0]
        celular = str(numbers[1]) + "-" + str(numbers[2])

        preference = Payment.mp.create_preference(
            {
                "items": [
                    {
                        "title": f"Doação para o casamemento de Felipe e Wendy",
                        "description": f"Doação de {document['name']} para o casamemento de Felipe e Wendy no valor de {document['price']}",
                        "quantity": 1,
                        "currency_id": "BRL",
                        "unit_price": document["price"],
                    }
                ],
                "payer": {
                    "name": f"{document['name']}",
                    "phone": {"area_code": codigo, "number": celular},
                },
            }
        )
        self.status = preference["status"]
        response = preference["response"]
        print(status)
        self._id = response["id"]
        self._url = response["init_point"]

    @property
    def pay_id(self):
        return self._id

    @property
    def url(self):
        return self._url