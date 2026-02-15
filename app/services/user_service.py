from ..extensions import db
from ..models.user import User

def create_user(name: str) -> User:
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return user

def list_users() -> list[User]:
    return User.query.order_by(User.id).all()
