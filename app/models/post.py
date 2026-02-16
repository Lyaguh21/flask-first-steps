from ..extensions import db
from datetime import datetime

post_likes = db.Table(
    "post_likes",
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
)

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30))
    description = db.Column(db.String(30))
    likes = db.relationship("User", secondary=post_likes, lazy="dynamic")
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False) 