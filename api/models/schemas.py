from datetime import date

from pydantic import BaseModel


class CreditCardBase(BaseModel):
    exp_date: str
    holder: str
    number: str
    cvv: str


class CreditCardCreate(CreditCardBase):
    pass


class CreditCardDetail(BaseModel):
    id: int
    exp_date: date
    holder: str
    number: str
    cvv: str
    brand: str
    created_at: date

    class Config:
        orm_mode = True
