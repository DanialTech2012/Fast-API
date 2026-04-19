from app.database import SessionLocal
from app.models import Wallet


BALANCE = {
    "cash" : 1000,
    "cash2" : 15000,
}

def is_wallet_exist(db, wallet_name):
        return db.query(Wallet).filter(wallet_name == wallet_name).first() is not None
     
    
def get_wallet_by_name(db, wallet_name):
        wallet = db.query(Wallet).filter(wallet_name == wallet_name).first()
        return wallet

def create_wallet(db, wallet_name, amount):
        wallet = Wallet(name=wallet_name, balance=amount)
        db.add(wallet)
        db.commit()
        db.refresh(wallet)
        return wallet


def add_income(db, wallet_name, amount):
        wallet = db.query(Wallet).filter(wallet_name == wallet_name).first()
        wallet.balance += amount
        db.commit()
        return wallet


def add_expense(db, wallet_name, amount):
        wallet = db.query(Wallet).filter(wallet_name == wallet_name).first()
        wallet.balance += amount
        db.commit()
        return wallet
