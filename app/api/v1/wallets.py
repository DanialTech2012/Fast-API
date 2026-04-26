from app.models import User
from app.schemas import WalletRequest

from app.service import wallets as wallets_service

from fastapi import APIRouter

router = APIRouter()
from app.dependency import get_current_user, get_db

from sqlalchemy.orm import Session
from fastapi import APIRouter ,Depends

router = APIRouter()


@router.get("/balance")
def get_balance(wallet : WalletRequest, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return wallets_service.get_balance(wallet=wallet, db=db, current_user=current_user)
            
@router.post("/wallet/{wallet_name}")
def create_wallet(wallet: WalletRequest, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return wallets_service.create_wallet(create_request=wallet, db=db, current_user=current_user)