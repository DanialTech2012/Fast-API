from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel, Field, field_validator

from app.api.v1.wallets import router as wallet_router
from app.api.v1.operation import router as operations_router


app = FastAPI()

app.include_router(wallet_router, prefix='/api/v1', tags=["Wallet"])
app.include_router(operations_router, prefix='/api/v1', tags=["Operations"]) 



@app.get("/health")
def health_checker():
    return Response(status_code=200)



