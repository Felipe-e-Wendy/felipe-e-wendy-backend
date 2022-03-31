from pydantic import BaseModel, constr, PositiveFloat

NameType = constr(max_length=50)

WhatsAPPType = constr(  # regex for (99) 99999-9999
    regex=r"^(\([0-9]{2}\))\s([9]{1})?([0-9]{4})-([0-9]{4})$"
)

MsgType = constr(max_length=140)


class FromForm(BaseModel):
    name: NameType
    wpp: WhatsAPPType
    price: PositiveFloat
    msg: MsgType
    token: str
