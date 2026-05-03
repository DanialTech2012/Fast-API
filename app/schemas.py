from decimal import Decimal

from pydantic import BaseModel, Field, field_validator

from datetime import datetime

from app.emun import CurrencyEnum


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

class WalletRequest(BaseModel):
    wallet : str = Field(..., max_length=127)
    amount : int
    currency : CurrencyEnum = CurrencyEnum.TENGE

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




class UserRequest(BaseModel):
    login : str = Field(..., max_length=127)

class UserResponse(UserRequest):
    model_config = {"from_attributes" : True}
    id : int

class WalletResponse(BaseModel):
    model_config = {"from_attributes" : True}

    id : int
    name : str
    balance : Decimal
    currency : CurrencyEnum
        

class OperationResponse(BaseModel):
     model_config =  {"from_attributes" : True}

     id : int
     wallet_id : int
     type : str
     amount : Decimal
     currency : CurrencyEnum
     category : str | None
     subcategory : str | None
     created_at : datetime