from flask import Blueprint, request, jsonify

from app.models.user import User
from ..services.posts_service import create_post, delete_like, get_post_by_id, list_posts, set_like

from app.models.post import Post

posts_bp = Blueprint("posts", __name__)

@posts_bp.post("/posts")
def post_post():
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    author = (data.get("author_id") or None)
    description = (data.get("description") or "").strip()
   
    if not (title):
        return jsonify({"error": "Заголовок не задан"},400)
    if not (description):
        return jsonify({"error": "Описание не задано"},400)
    if not (author):
        return jsonify({"error": "Id автора поста не задано"},400)
    
    post = create_post(author , title, description)
    return jsonify({"id": post.id, "author_id": post.author_id, "title": post.title, "created_at": post.created_at, "is_liked": False, "likes": 0}), 201

@posts_bp.get("/posts")
def get_posts():
    posts = list_posts()
    return jsonify([{id: post.id, "title": post.title, "description": post.description, "created_at": post.created_at, "likes": post.likes.count(), "is_liked": post.likes.filter(User.id == post.author_id).count() > 0 } for post in posts]), 200

@posts_bp.get("/posts/<int:post_id>")
def get_post(post_id):
    post = get_post_by_id(post_id)

    if not post:
        return jsonify({"error": "post not found"}), 400
    
    return jsonify({"id": post.id, "author_id": post.author_id, "title": post.title, "created_at": post.created_at, "is_liked": False, "likes": 0}), 200    

@posts_bp.post("/posts/<int:post_id>/like")
def like_post(post_id):
    post = get_post_by_id(post_id)

    if not post:
        return jsonify({"error": "post not found"}), 404
    
    data = request.get_json(silent=True) or {}
    user_id = (data.get("user_id") or None)
    if not (user_id):
        return jsonify({"error": "Id пользователя не задано"}), 400
    
    updated_post = set_like(post, user_id)
    return jsonify({"id": updated_post.id, "author_id": updated_post.author_id, "title": updated_post.title, "created_at": updated_post.created_at, "is_liked": True, "likes": updated_post.likes.count()}), 200

@posts_bp.delete("/posts/<int:post_id>/like")
def unlike_post(post_id):
    post = get_post_by_id(post_id)

    if not post:
        return jsonify({"error": "post not found"}), 404
    
    data = request.get_json(silent=True) or {}
    user_id = (data.get("user_id") or None)
    if not (user_id):
        return jsonify({"error": "Id пользователя не задано"}), 400
    
    updated_post = delete_like(post, user_id)
    return jsonify({"id": updated_post.id, "author_id": updated_post.author_id, "title": updated_post.title, "created_at": updated_post.created_at, "is_liked": False, "likes": updated_post.likes.count()}), 200