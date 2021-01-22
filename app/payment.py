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


{
    "status": 201,
    "response": {
        "additional_info": "",
        "auto_return": "",
        "back_urls": {"failure": "", "pending": "", "success": ""},
        "binary_mode": False,
        "client_id": "6087966002603691",
        "collector_id": 153711380,
        "coupon_code": None,
        "coupon_labels": None,
        "date_created": "2021-01-21T22:49:21.278+00:00",
        "date_of_expiration": None,
        "expiration_date_from": None,
        "expiration_date_to": None,
        "expires": False,
        "external_reference": "",
        "id": "153711380-c3a0326a-74e6-4571-8c8a-1b05cc96cc17",
        "init_point": "https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=153711380-c3a0326a-74e6-4571-8c8a-1b05cc96cc17",
        "internal_metadata": None,
        "items": [
            {
                "id": "",
                "category_id": "",
                "currency_id": "BRL",
                "description": "Doação de Usuário Teste MP para o casamemento de Felipe e Wendy no valor de 580.0",
                "title": "Doação para o casamemento de Felipe e Wendy",
                "quantity": 1,
                "unit_price": 580,
            }
        ],
        "marketplace": "NONE",
        "marketplace_fee": 0,
        "metadata": {},
        "notification_url": None,
        "operation_type": "regular_payment",
        "payer": {
            "phone": {"area_code": "99", "number": "99999-9999"},
            "address": {"zip_code": "", "street_name": "", "street_number": None},
            "email": "",
            "identification": {"number": "", "type": ""},
            "name": "Usuário Teste MP",
            "surname": "",
            "date_created": None,
            "last_purchase": None,
        },
        "payment_methods": {
            "default_card_id": None,
            "default_payment_method_id": None,
            "excluded_payment_methods": [{"id": ""}],
            "excluded_payment_types": [{"id": ""}],
            "installments": None,
            "default_installments": None,
        },
        "processing_modes": None,
        "product_id": None,
        "redirect_urls": {"failure": "", "pending": "", "success": ""},
        "sandbox_init_point": "https://sandbox.mercadopago.com.br/checkout/v1/redirect?pref_id=153711380-c3a0326a-74e6-4571-8c8a-1b05cc96cc17",
        "site_id": "MLB",
        "shipments": {
            "default_shipping_method": None,
            "receiver_address": {
                "zip_code": "",
                "street_name": "",
                "street_number": None,
                "floor": "",
                "apartment": "",
                "city_name": None,
                "state_name": None,
                "country_name": None,
            },
        },
        "total_amount": None,
        "last_updated": None,
    },
}
