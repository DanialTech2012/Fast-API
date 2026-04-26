from sqlalchemy.orm import Session

 
from app.schemas import UserRequest, UserResponse
from app.service import users as users_service
from app.repository import user as UserRepository
from app.dependency import get_current_user
from app.dependency import get_db

from fastapi import APIRouter ,Depends



router = APIRouter()

@router.post("/users", response_model=UserResponse)
def create_user(payload : UserRequest, db: Session = Depends(get_db)):
    return users_service.create_user(db = db, payload=payload)

@router.get("/users/me", response_model=UserResponse)
def get_current_user(current_user = Depends(get_current_user)):
    return UserResponse.model_validate(current_user)