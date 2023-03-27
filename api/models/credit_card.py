from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class CreditCard(Base):
    __tablename__ = "credit_card"

    id = Column(Integer, primary_key=True, index=True)
    exp_date = Column(DateTime, nullable=False)
    holder = Column(String, nullable=False)
    number = Column(String, nullable=False, unique=True)
    cvv = Column(String, nullable=True)
    brand = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
