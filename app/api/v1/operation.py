from datetime import datetime

from sqlalchemy.orm import Session


from app.models import User
from app.schemas import OperationRequest, OperationResponse
from app.service import operation as operations_service
from app.dependency import get_current_user, get_db

from fastapi import APIRouter ,Depends, Query

from fastapi import APIRouter

router = APIRouter()

@router.post("/operation/income", response_model=OperationResponse)
def income_operation(operation : OperationRequest ,db: Session = Depends(get_db),  current_user = Depends(get_current_user)):
    return operations_service.income_operation(operation=operation, db = db, current_user = current_user)
   
@router.post("/operation/expense", response_model=OperationResponse)
def expense_opration(operation : OperationRequest, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return operations_service.expense_operation(operation=operation, db = db, current_user = current_user)

@router.get("/operations", response_model=list[OperationResponse])
def get_operations_list(
    wallet_id : int | None = Query(None),
    date_from : datetime | None = Query(None),
    date_to : datetime =Depends(get_current_user),
    user : User = Depends(get_current_user),
    db : Session = Depends(get_db)
):
    return operations_service.get_operation_list(wallet_id=wallet_id, date_from=date_from, date_to=date_to, user=user, db=db)