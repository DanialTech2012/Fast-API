from app.models import User

def get_user(db, login):
    user = db.query(User).filter(User.login == login).first()
    return user

def create_user(db, login : int):
    user = User(login=login)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user