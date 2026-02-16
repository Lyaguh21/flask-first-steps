from ..extensions import db
from ..models.post import Post
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

def create_post(title: str, description: str, ) -> Post:
    created_at = datetime.now()
    post = Post(title=title, description=description, created_at=created_at)
    db.session.add(post)
    db.session.commit()
    return post