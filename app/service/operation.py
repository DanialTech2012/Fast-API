from fastapi import HTTPException

from app.database import SessionLocal
from app.models import User
from app.repository.wallets import BALANCE
from app.schemas import OperationRequest, OperationResponse
from app.repository import wallets as wallets_repository

from app.repository import operations as operation_repository

def income_operation(operation : OperationRequest,db, current_user : User) -> OperationResponse:
    if not wallets_repository.is_wallet_exist(db, wallet_name=operation.wallet, user_id=current_user.id):
        raise HTTPException(status_code=400,
                        detail=f"wallet is not in db")
    
    wallet = wallets_repository.add_income(db, wallet_name=operation.wallet, amount=operation.amount,  user_id=current_user.id)

    operation_add = operation_repository.create_operation(
        db,
        wallet_id=wallet.id,
        type= "income",
        amount=operation.amount,
        currency=wallet.currency,
        catrgory=operation.description,
        category=operation.description 
    )
    db.commit()

    return OperationResponse.model_validate(operation_add)


def expense_operation(operation : OperationRequest,db, current_user : User) -> OperationResponse:
    if not wallets_repository.is_wallet_exist(db, wallet_name=operation.wallet, user_id=current_user.id):
        raise HTTPException(status_code=400,
                            detail=f"wallet is not in db")
    wallet = wallets_repository.add_expense(db, wallet_name=operation.wallet, amount=operation.amount, user_id=current_user.id)

    operation_add = operation_repository.create_operation(
        db,
        wallet_id=wallet.id,
        type= "expense",
        amount=operation.amount,
        currency=wallet.currency,
        catrgory=operation.description,
        category=operation.description 
    )
    db.commit()

    return OperationResponse.model_validate(operation_add)\
    
def get_operation_list(db, wallet_id, user, date_from, date_to):
    if wallet_id:
        wallet = wallets_repository.get_wallet_by_id(wallet_id=wallet_id, db=db, user_id=user.id)

        if not wallet:
            raise HTTPException(status_code=400, detail="Wallet not found")
        
        wallets_ids = [wallet.id]
    else:
        wallets = wallets_repository.get_all_wallets(db, user_id=user.id)

        wallets_ids = [w.id for w in wallets]

    operations = operation_repository.get_operation_list(db=db, date_from=date_from, date_to=date_to, wallets_ids=wallets_ids)

    result = []

    for operation in operation:
        result.append(OperationResponse.model_validate(operation))

    return result