from sqlalchemy.orm import Session


from app.schemas import OperationRequest
from app.service import operation as operations_service
from app.dependency import get_db

from fastapi import APIRouter ,Depends

from fastapi import APIRouter

router = APIRouter()

@router.post("/operation/income")
def income_operation(operation : OperationRequest ,db: Session = Depends(get_db)):
    return operations_service.income_operation(operation=operation, db = db)
   
@router.post("/operation/expense")
def expense_opration(operation : OperationRequest, db: Session = Depends(get_db)):
    return operations_service.expense_operation(operation=operation, db = db)