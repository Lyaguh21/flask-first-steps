from app.models.user import User
from ..extensions import db
from ..models.post import Post
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

def create_post(author_id: int, title: str, description: str, ) -> Post:

    post = Post(author_id=author_id, title=title, description=description)
    db.session.add(post)
    db.session.commit()
    return post

def list_posts() -> list[Post]:
    return Post.query.order_by(Post.id).all()

def get_post_by_id(post_id: int) -> Post | None:
    return db.session.get(Post, post_id)

def set_like(post: Post, user_id: int) -> Post:
    user = db.session.get(User, user_id)
    if post.likes.filter_by(id=user_id).count() > 0:
        return post
    else:
        post.likes.append(user)
        db.session.commit()
        return post
    
def delete_like(post: Post, user_id: int) -> Post:
    user = db.session.get(User, user_id)
    if post.likes.filter_by(id=user_id).count() > 0:
        post.likes.remove(user)
        db.session.commit()
        return post
    else:
        return post