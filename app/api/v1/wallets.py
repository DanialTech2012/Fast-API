from app.schemas import WalletRequest
from app.service import wallets as wallets_service

from fastapi import APIRouter

router = APIRouter()




@router.get("/balance")
def get_balancce(wallet : WalletRequest):
    return wallets_service.get_balancce(wallet=wallet)
            
@router.post("/wallet/{wallet_name}")
def recieve_money(wallet : WalletRequest):
    return wallets_service.recieve_money(wallet=wallet)