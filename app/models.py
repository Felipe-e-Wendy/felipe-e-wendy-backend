from pydantic import BaseModel, constr, PositiveFloat

_wpp_len = len("(99) 99999-9999")


class FromForm(BaseModel):
    name: constr(max_length=50)
    wpp: constr(max_length=_wpp_len, min_length=_wpp_len)
    price: PositiveFloat
    msg: constr(max_length=140)
    token: str


class Schema(BaseModel):
    ...
