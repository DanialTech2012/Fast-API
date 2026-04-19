from fastapi import HTTPException

from app.database import SessionLocal
from app.schemas import WalletRequest

from app.repository import wallets as wallet_repository

from app.repository import wallets 



def get_balance(wallet: WalletRequest):
    db = SessionLocal()
    try:
        if wallet.wallet is None:
            return Response(status_code=200,
                            content=f"Your balance across all wallets is {sum([i.balance for i in wallet_repository.get_all_wallets(db)])}")

        if not wallet_repository.is_wallet_exist(db, wallet.wallet):
            return HTTPException(status_code=400,
                                detail=f"Wallet with name {wallet.wallet} is not found")
        
        db_wallet = wallet_repository.get_wallet_by_name(db, wallet_name=wallet.wallet)
        
        return {"wallet_name" : wallet.wallet,
                "balance" : wallet_repository.get_wallet_by_name(db, wallet_name=wallet.wallet).balance}
    finally:
        db.close()

def create_wallet(create_request: WalletRequest):
    db = SessionLocal()
    try:
        if wallet_repository.is_wallet_exist(db, create_request.wallet):
            raise HTTPException(status_code=400,
                            detail="wallet already exists")
        
        wallet_repository.create_wallet(db, wallet_name=create_request.wallet, amount=create_request.amount)

        return {"wallet_name" : create_request.wallet, "amount" : create_request.amount, "detail" : "Wallet is created"}
    finally:
        db.close()
