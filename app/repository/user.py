from app.models import User

def create_user(db, login : int):
    user = User(login=login)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user