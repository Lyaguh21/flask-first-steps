from flask import Blueprint, request, jsonify
from ..services.posts_service import create_post

from app.models.post import Post

posts_bp = Blueprint("posts", __name__)

@posts_bp.post("/posts")
def post_post():
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    description = (data.get("description") or "").strip()
   
    if not (title):
        return jsonify({"error": "Заголовок не задан"},400)
    if not (description):
        return jsonify({"error": "Описание не задано"},400)
    
    post = create_post(title, description)
    return jsonify({"id": post.id, "title": post.title, "created_at": post.created_at, "likes": [], "likes_count": 0}), 201