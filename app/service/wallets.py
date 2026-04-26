from fastapi import HTTPException

from app.database import SessionLocal
from app.models import User
from app.schemas import WalletRequest

from app.repository import wallets as wallet_repository

from app.repository import wallets 



def get_balance(wallet: WalletRequest,db, current_user : User):
    if wallet.wallet is None:
        return Response(status_code=200,
                        content=f"Your balance across all wallets is {sum([i.balance for i in wallet_repository.get_all_wallets(db, user_id=current_user.id)])}")

    if not wallet_repository.is_wallet_exist(db, wallet.wallet, current_user.id):
        return HTTPException(status_code=400,
                            detail=f"Wallet with name {wallet.wallet} is not found")
    
    db_wallet = wallet_repository.get_wallet_by_name(db, wallet_name=wallet.wallet, user_id=current_user.id)
    
    return {"wallet_name" : wallet.wallet,
            "balance" : db_wallet.balance}


def create_wallet(create_request: WalletRequest,db, current_user: User):
    if wallet_repository.is_wallet_exist(db, create_request.wallet,  user_id=current_user.id):
        raise HTTPException(status_code=400,
                        detail="wallet already exists")
    
    wallet_repository.create_wallet(db, wallet_name=create_request.wallet, amount=create_request.amount,  user_id=current_user.id)

    return {"wallet_name" : create_request.wallet, "amount" : create_request.amount, "detail" : "Wallet is created"}
