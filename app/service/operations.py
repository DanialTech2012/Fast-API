from fastapi import HTTPException

from app.database import SessionLocal
from app.repository.wallets import BALANCE
from app.schemas import OperationRequest
from app.repository import wallets as wallets_repository


def income_operation(operation : OperationRequest):
    db = SessionLocal()
    try:
        if not wallets_repository.is_wallet_exist(db, wallet_name=operation.wallet):
            raise HTTPException(status_code=400,
                            detail=f"wallet is not in db")
        
        wallet = wallets_repository.add_income(db, wallet_name=operation.wallet, amount=operation.amount)

        return{
            "wallet_name" : operation.wallet,
            "amount" : operation.amount,
            "description" : operation.description,
            "new_balance" : wallet.balance,
            "message" : "Amount is expensed to balance"
        }
    finally:
        db.close()

def expense_opration(operation : OperationRequest):
    db = SessionLocal()
    try:
        if not wallets_repository.is_wallet_exist(db, wallet_name=operation.wallet):
            raise HTTPException(status_code=400,
                                detail=f"wallet is not in db")
        wallet = wallets_repository.add_expense(db, wallet_name=operation.wallet, amount=operation.amount)

        return{
            "wallet_name" : operation.wallet,
            "amount" : operation.amount,
            "description" : operation.description,
            "new_balance" : wallet.balance,
            "message" : "Amount is deducted to balance"
        }
    finally:
        db.close()

