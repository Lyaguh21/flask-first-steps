from ..extensions import db
from ..models.user import User
from sqlalchemy.exc import SQLAlchemyError

def create_user(name: str) -> User:
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return user

def list_users() -> list[User]:
    return User.query.order_by(User.id).all()

def get_user_by_id(user_id:int) -> User | None:
    return db.session.get(User, user_id)

def update_user(user_id: int, new_name: str) -> User | None:
    user = db.session.get(User, user_id)
    if not user:
        return None

    user.name = new_name
    db.session.commit()
    return user

def delete_user_by_id(user_id: int) -> bool:
    user = db.session.get(User, user_id)
    if not user:
        return False

    try:
        db.session.delete(user)
        db.session.commit()
        return True
    except SQLAlchemyError:
        db.session.rollback()
        return False

