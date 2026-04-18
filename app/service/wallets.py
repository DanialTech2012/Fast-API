from fastapi import HTTPException

from app.schemas import WalletRequest

from app.repository import wallets as wallets_repository

from app.repository import wallets 


def get_balancce(wallet : WalletRequest):
    if wallet.wallet is None:
        return Response(status_code=200,
                        content=f"Your balance across all wallets is {sum(BALANCE.values())}")

    if wallets_repository.is_wallet_exist(wallet.wallet):
        return HTTPException(status_code=400,
                             detail=f"Wallet with name {wallet.wallet} is not found")
    
    return {"wallet_name" : wallet.wallet,
            "balance" : wallets_repository.get_wallet_by_name(wallet_name=wallet.wallet).get[wallet.wallet]}

def create_wallet(create_request : WalletRequest):
    if wallets_repository.is_wallet_exist(create_request.wallet):
        raise HTTPException(status_code=400,
                           detail="wallet already exists")
    
    wallets_repository.create_wallet(wallet_name=create_request.wallet, amount=create_request.amount)

    return {"wallet_name" : create_request.wallet, "amount" : create_request.amount, "detail" : "Wallet is created"}