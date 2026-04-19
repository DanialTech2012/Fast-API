from app.schemas import WalletRequest

from app.service import wallets as wallets_service

from fastapi import APIRouter

router = APIRouter()




router = APIRouter()


@router.get("/balance")
def get_balance(wallet : WalletRequest):
    return wallets_service.get_balance(wallet=wallet)
            
@router.post("/wallet/{wallet_name}")
def create_wallet(wallet: WalletRequest):
    return wallets_service.create_wallet(wallet=wallet)

from app.schemas import WalletRequest

from app.service import wallets as wallets_service

from fastapi import APIRouter


router = APIRouter()


@router.post("/balance")
def get_balance(wallet : WalletRequest):
    return wallets_service.get_balance(wallet=wallet)
            
@router.post("/wallet/{wallet_name}")
def create_wallet(wallet: WalletRequest):
    return wallets_service.create_wallet(create_request=wallet)
