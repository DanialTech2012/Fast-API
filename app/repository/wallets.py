from app.database import SessionLocal
from app.models import Wallet


BALANCE = {
    "cash" : 1000,
    "cash2" : 15000,
}

def is_wallet_exist(db, wallet_name, user_id : int):
        return db.query(Wallet).filter(wallet_name == wallet_name, Wallet.user_id == user_id).first() is not None
     
    
def get_wallet_by_name(db, wallet_name, user_id : int):
        wallet = db.query(Wallet).filter(wallet_name == wallet_name, Wallet.user_id == user_id).first()
        return wallet

def get_all_wallets(db, user_id : int):
        return db.query(Wallet).filter(Wallet.user_id == user_id).all()

def create_wallet(db, wallet_name, amount, user_id : int):
        wallet = Wallet(name=wallet_name, balance=amount, user_id=user_id)
        db.add(wallet)
        db.commit()
        db.refresh(wallet)
        return wallet


def add_income(db, wallet_name, amount, user_id : int):
        wallet = db.query(Wallet).filter(wallet_name == wallet_name, Wallet.user_id == user_id).first()
        wallet.balance += amount
        db.commit()
        return wallet


def add_expense(db, wallet_name, amount, user_id : int):
        wallet = db.query(Wallet).filter(wallet_name == wallet_name, Wallet.user_id == user_id).first()
        wallet.balance -= amount
        db.commit()
        return wallet
