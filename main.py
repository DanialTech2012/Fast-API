from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

BALANCE = {
    "cash" : 10000,
    "cash2" : 15000
}

class OperationRequest(BaseModel):
    wallet : str = Field(..., max_length=127)
    wallet : str
    amount : int
    description : str | None

    @field_validator('amount')
    def amount_be_positive(cls, v : float) -> float:
        if v <=0:
            raise ValueError("Amount must be positive")
        
        return v
    
    @field_validator('wallet')
    def wallet_name_not_empty(cls, v : str) -> str:
        v = v.strip()

        if not v:
            raise ValueError("Wallet name cannot be empty")
        
        return v
    
class CreateWalletRequest(BaseModel):
    wallet : str = Field(..., max_length=127)
    amount : int

    @field_validator('amount')
    def amount_be_positive(cls, v : float) -> float:
        if v <=0:
            raise ValueError("Amount must be positive")
        
        return v
    
    @field_validator('wallet')
    def wallet_name_not_empty(cls, v : str) -> str:
        v = v.strip()

        if not v:
            raise ValueError("Wallet name cannot be empty")
        
        return v

@app.get("/health")
def health_checker():
    return Response(status_code=200)

@app.get("/balance")
def get_balance(wallet_name : str | None = None):
    if wallet_name is None:
        return Response(status_code=200,
                        content=f"Your balance across all wallets is {sum(BALANCE.values())}")

    if wallet_name not in BALANCE:
        return HTTPException(status_code=400,
                             detail=f"Wallet with name {wallet_name} is not found")
    
    return {"wallet_name" : wallet_name,
            "balance" : BALANCE[wallet_name]}




@app.post("/wallet/{wallet_name}")
def reseive_money(wallet_name : str, amount : int):
    if wallet_name in BALANCE:
        raise HTTPException(status_code=400,
                            detail="Wallet is arleady exist")
    
    BALANCE[wallet_name] = amount

    return {"wallet_name" : wallet_name, "amount" : amount, "detail" : "Wallrt is created"}





@app.post("/operations/income")
def income_operation(operation : OperationRequest):
    if operation.wallet not in BALANCE:
        raise HTTPException(status_code=400,
                            detail=f"Wallet with wallet name {operation.wallet} is not found")

    BALANCE[operation.wallet] += operation.amount

    return {
        "wallet_name" : operation.wallet,
        "amount" : operation.amount,
        "description" : operation.description,
        "new_balance" : BALANCE[operation.wallet],
        "message" : "Amount is added to balance"
    }

@app.post("/operations/expense")
def expense_operation(operation : OperationRequest):
    if operation.wallet not in BALANCE:
        raise HTTPException(status_code=400,
                            detail=f"Wallet with wallet name {operation.wallet} is not found")
    
    BALANCE[operation.wallet] -= operation.amount

    return {
        "wallet_name" : operation.wallet,
        "amount" : operation.amount,
        "description" : operation.description,
        "new_balance" : BALANCE[operation.wallet],
        "message" : "Amount is deducted to balance"
    }
