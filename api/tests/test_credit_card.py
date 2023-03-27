from fastapi.testclient import TestClient

from api.core.settings import settings
from api.database.connection import SessionLocal
from api.models.credit_card import CreditCard
from api.models.schemas import CreditCardCreate
from main import app

client = TestClient(app)


def test_auth_token():
    response = client.post(
        "/login",
        params={
            "username": settings.DB_USER,
            "password": settings.DB_PASSWORD,
        },
    )
    assert response.status_code == 200
    return response.json()["access_token"]


def test_create_credit_card():
    credit_card = CreditCardCreate(
        exp_date="10/2027",
        holder="John Doe",
        number="5454545454545454",
        cvv="123",
        brand="visa",
    )
    db = SessionLocal()
    db.query(CreditCard).filter(
        CreditCard.number == credit_card.number
    ).delete()
    db.commit()
    db.close()

    response = client.post(
        "/credit-card/",
        json=credit_card.dict(),
        headers={"Authorization": f"Bearer {test_auth_token()}"},
    )
    assert response.status_code == 200
    assert response.json()["number"] == "5454545454545454"
    return response.json()["id"]


def test_get_credit_card():
    credit_card_id = test_create_credit_card()
    response = client.get(
        f"/credit-card/{credit_card_id}",
        headers={"Authorization": f"Bearer {test_auth_token()}"},
    )
    assert response.status_code == 200
    assert response.json()["number"] == "5454545454545454"


def test_get_credit_cards():
    response = client.get(
        "/credit-card/",
        headers={"Authorization": f"Bearer {test_auth_token()}"},
    )
    assert response.status_code == 200
