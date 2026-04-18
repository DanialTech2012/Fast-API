

from app.schemas import OperationRequest
from app.service import operation as operations_service

from fastapi import APIRouter

router = APIRouter()

@router.post("/operation/income")
def income_operation(operation : OperationRequest):
    return operations_service.income_operation(operation=operation)
   
@router.post("/operation/expense")
def expense_opration(operation : OperationRequest):
    return operations_service.expense_operation(operation=operation)