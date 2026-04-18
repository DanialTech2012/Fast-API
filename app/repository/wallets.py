BALANCE = {
    "cash" : 1000,
    "cash2" : 15000,
}

def is_wallet_exists(wallet_name):
    return wallet_name not in BALANCE
    
def get_wallet_by_name(wallet_name):
    return {wallet_name : BALANCE[wallet_name]}
    
def create_wallet(wallet_name, amount) :
    BALANCE[wallet_name] = amount

def add_income(wallet_name, amount):
    BALANCE[wallet_name] += amount


def add_expense(wallet_name, amount):
    BALANCE[wallet_name] += amount