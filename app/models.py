from pydantic import BaseModel, constr, PositiveFloat

class FromForm(BaseModel):
    name: constr(max_length=50)
    wpp: constr(regex=r"^(\([0-9]{2}\))\s([9]{1})?([0-9]{4})-([0-9]{4})$") #regex for (99) 99999-9999
    price: PositiveFloat
    msg: constr(max_length=140)
    token: str


class Schema(BaseModel):
    ...
