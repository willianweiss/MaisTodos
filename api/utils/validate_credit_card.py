import calendar
from datetime import datetime, timedelta

from creditcard import CreditCard
from creditcard.exceptions import BrandNotFound
from fastapi import HTTPException


def validate_credit_card(
    number: str,
    exp_date: str,
    holder: str,
    cvv: str,
) -> dict:
    try:
        exp_date = datetime.strptime(exp_date, "%m/%Y")
        last_day_of_month = calendar.monthrange(exp_date.year, exp_date.month)[
            1
        ]
        exp_date = exp_date.replace(day=last_day_of_month)
        if exp_date < datetime.today():
            raise HTTPException(
                status_code=400,
                detail="expiration date must be greater than or equal to today",
            )
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="invalid expiration date format, must be in the format MM/YYYY",
        )

    if len(holder) < 2:
        raise ValueError("holder name must have at least 2 characters")

    cc = CreditCard(number)
    if not cc.is_valid():
        raise HTTPException(status_code=400, detail="invalid card number")

    try:
        brand = cc.get_brand()
    except BrandNotFound:
        raise HTTPException(status_code=400, detail="invalid card brand")

    return {
        "exp_date": exp_date.strftime("%Y-%m-%d"),
        "holder": holder,
        "number": number,
        "cvv": cvv,
        "brand": brand,
    }
