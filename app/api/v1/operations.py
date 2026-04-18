
from app.schemas import OperationRequest
from app.service import operations as operation_service
from fastapi import APIRouter

router = APIRouter()

@router.post("/operation/income")
def income_operation(operation : OperationRequest):
    return operation_service.income_operation(operation=operation)
@router.post("/operation/expense")
def expense_opration(operation : OperationRequest):
    return operation_service.expense_operation(operation=operation)