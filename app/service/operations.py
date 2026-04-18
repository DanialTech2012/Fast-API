from fastapi import HTTPException

from app.repository.wallets import BALANCE
from app.schemas import OperationRequest
from app.repository import wallets as wallets_repository


def income_operation(operation : OperationRequest):

    if not wallets_repository.is_wallet_exist(wallet_name=operation.wallet):
        raise HTTPException(status_code=400,
                            detail=f"wallet is not in db")
    
    wallets_repository.add_expense(wallet_name=operation.wallet, amount=operation.amount)

    return{
        "wallet_name" : operation.wallet,
        "amount" : operation.amount,
        "description" : operation.description,
        "new_balance" : wallets_repository.get_wallet_by_name(wallet_name=operation.wallet).get(operation.wallet),
        "message" : "Amount is expensed to balance"
    }
def expense_opration(operation : OperationRequest):
    if not wallets_repository.is_wallet_exist(wallet_name=operation.wallet):
        raise HTTPException(status_code=400,
                            detail=f"wallet is not in db")
    wallets_repository.add_expense(wallet_name=operation.wallet, amount=operation.amount)

    return{
        "wallet_name" : operation.wallet,
        "amount" : operation.amount,
        "description" : operation.description,
        "new_balance" : wallets_repository.get_wallet_by_name(wallet_name=operation.wallet).get(operation.wallet),
        "message" : "Amount is deducted to balance"
    }
