from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel, Field, field_validator


app = FastAPI()

BALANCE = {
    "cash" : 1000,
    "cash2" : 15000,
}

class OperationRequest(BaseModel):
    wallet : str = Field(..., max_length=127)
    amount : int
    description : str | None 

    @field_validator('amount')
    def amount_must_be_positive(cls, v : float) -> float:

        if v <= 0:
                raise ValueError("Amount must be positive")
            
        return v
    
    @field_validator("wallet")
    def wallet_name_cannot_be_empty(cls, v :str) -> str:
        if not v:
            raise ValueError("Wallet name cannot be empty")
        
        return v

# class OperationRequest(BaseModel):
#     wallet : str = Field(..., max_length=127)
#     amount : int

#     @field_validator('amount')
#     def amount_must_be_positive(cls, v : float) -> float:

#         if v <= 0:
#                 return ValueError("Amount must be positive")
            
#         return v
    
#     @field_validator("wallet")
#     def wallet_name_cannot_be_empty(cls, v :str) -> str:
#         if not v:
#             raise ValueError("Wallet name cannot be empty")
        
#         return v


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
    if wallet_name in BALANCE:
        raise HTTPException(status_code=400,
                           detail="wallet already exists")
    
    BALANCE[wallet_name] = amount

    return {"walleet_name" : wallet_name, "amount" : amount, "detail" : "Wallet is created"}

@app.post("/operation/income")
def income_operation(operation : OperationRequest):
    if operation.wallet not in BALANCE:
        raise HTTPException(status_code=400,
                            detail=f"wallet is not in db")
    
    BALANCE[operation.wallet] += operation.amount
    return{
        "wallet_name" : operation.wallet,
        "amount" : operation.amount,
        "description" : operation.description,
        "new_balance" : BALANCE[operation.wallet],
        "message" : "Amount is expensed to balance"
    }

@app.post("/operation/expense")
def expense_opration(operation : OperationRequest):
    if operation.wallet not in BALANCE:
        raise HTTPException(status_code=400,
                            detail=f"wallet is not in db")
    BALANCE[operation.wallet] -= operation.amount
    return{
        "wallet_name" : operation.wallet,
        "amount" : operation.amount,
        "description" : operation.description,
        "new_balance" : BALANCE[operation.wallet],
        "message" : "Amount is deducted to balance"
    }














