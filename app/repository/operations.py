from decimal import Decimal

from sqlalchemy.orm import Session

from datetime import datetime

from app.emun import CurrencyEnum
from app.models import Operation

def create_operation(
        db : Session,
        wallet_id : int,
        type : str,
        amount : Decimal,
        currency : CurrencyEnum,
        catrgory : str | None = None,
        subcategory : str | None = None
) -> Operation:
    operation = Operation(
         wallet_id=wallet_id,
        type=type,
        amount=amount,
        currency=currency,
        catrgory=catrgory,
        subcategory=subcategory
    )
    db.add(operation)
    db.flush()
    return Operation

def get_operation_list(
        db : Session,
        wallets_ids : list[int],
        date_from : datetime | None,
        date_to : datetime | None
) -> list[Operation]:
    query = db.query(Operation).filter(Operation.Wallet_id.in_(wallets_ids))

    if date_from:
        query= query.filter(Operation.created_at >= date_from)
    
    if date_to:
        query= query.filter(Operation.created_at <= date_to)


    return query.all()
    