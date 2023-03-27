from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.auth.auth_bearer import JWTBearer
from api.database.connection import get_db
from api.models.credit_card import CreditCard
from api.models.schemas import CreditCardCreate, CreditCardDetail
from api.utils.validate_credit_card import validate_credit_card

router = APIRouter(
    tags=["credit_cards"],
    # dependencies=[Depends(JWTBearer())],
    responses={404: {"description": "Not found"}},
)


@router.post("/credit-card/", response_model=CreditCardDetail)
async def create_credit_card(
    credit_card: CreditCardCreate, db: Session = Depends(get_db)
):
    if (
        db.query(CreditCard)
        .filter(CreditCard.number == credit_card.number)
        .first()
    ):
        raise HTTPException(
            status_code=400, detail="Credit card already exists"
        )
    credit_card_validated = validate_credit_card(
        credit_card.number,
        credit_card.exp_date,
        credit_card.holder,
        credit_card.cvv,
    )
    db_card = CreditCard(**credit_card_validated)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


@router.get("/credit-card/", response_model=List[CreditCardDetail])
async def read_credit_cards(limit: int = 100, db: Session = Depends(get_db)):
    cards = db.query(CreditCard).limit(limit).all()
    return cards


@router.get("/credit-card/{credit_card_id}", response_model=CreditCardDetail)
async def read_credit_card(credit_card_id: int, db: Session = Depends(get_db)):
    db_card = (
        db.query(CreditCard).filter(CreditCard.id == credit_card_id).first()
    )
    if not db_card:
        raise HTTPException(status_code=404, detail="Credit card not found")
    return db_card
