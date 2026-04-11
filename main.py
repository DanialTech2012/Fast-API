from fastapi import FastAPI, HTTPException
from fastapi.responses import Response

app = FastAPI()

BALANCE = {
    "cash" : 1000,
    "cash2" : 15000,
}

@app.get("/health")
def health_checker():
    return Response(status_code=200)

@app.get("/balance")
def get_balancce(wallet_name : str | None = None):
    if wallet_name is None:
        return Response(status_code=200,
                        content=f"Your balance across all wallets is {sum(BALANCE.values())}")

    if wallet_name not in BALANCE:
        return HTTPException(status_code=400,
                             detail=f"Wallet with name {wallet_name} is not found")
    
    return {"wallet_name" : wallet_name,
            "balance" : BALANCE[wallet_name]}
            
@app.post("/wallet/{wallet_name}")
def recieve_money(wallet_name : str, amount : int):
    if wallet_name not in BALANCE:
        BALANCE[wallet_name] = 0
        return {"detail" : f"Wallet with name {wallet_name} is created"}
    
    BALANCE [wallet_name] += amount
    return {"wallet_name" : {wallet_name},
            "detail" : f"Your wallet {wallet_name} is top up with {amount}"}

