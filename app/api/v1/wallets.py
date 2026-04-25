from app.schemas import WalletRequest

from app.service import wallets as wallets_service

from fastapi import APIRouter

router = APIRouter()
from app.dependency import get_db

from sqlalchemy.orm import Session

from fastapi import APIRouter ,Depends

router = APIRouter()


@router.get("/balance")
def get_balance(wallet : WalletRequest, db: Session = Depends(get_db)):
    return wallets_service.get_balance(wallet=wallet, db=db)
            
@router.post("/wallet/{wallet_name}")
def create_wallet(wallet: WalletRequest, db: Session = Depends(get_db)):
    return wallets_service.create_wallet(wallet=wallet, db=db)