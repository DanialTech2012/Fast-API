from app.repository import user as user_repository
from app.schemas import UserResponse


def create_user(db, payload):
    user = user_repository.create_user(db=db, login=payload.login)
    print(user.id)
    return UserResponse.model_validate(user)