from decimal import Decimal

from sqlalchemy import ForeignKey

from datetime import datetime

from app.database import Base

from sqlalchemy.orm import Mapped, mapped_column

from app.emun import CurrencyEnum

class User(Base):
    __tablename__ = "user"

    id : Mapped[int] =  mapped_column(primary_key=True)
    login : Mapped[str] = mapped_column(unique=True)

class Wallet(Base):
    __tablename__ = "wallet"

    id :Mapped[int] =  mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(unique=True)
    balance : Mapped[Decimal]

    user_id : Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)

    currency : Mapped[CurrencyEnum]


class Operation(Base):
    __tablename__ = "operation"

    id : Mapped[int] = mapped_column(primary_key=True)
    Wallet_id : Mapped[int] = mapped_column(ForeignKey("wallet.id"), nullable=False)
    type : Mapped[str]
    currency : Mapped[CurrencyEnum]
    amount : Mapped[str | None] = mapped_column(default=None)
    subcategoty : Mapped[str | None] = mapped_column(default=None)
    created_at : Mapped[datetime] = mapped_column(default= lambda: datetime.now())
