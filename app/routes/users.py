from flask import Blueprint, request, jsonify

from app.models.user import User
from ..services.user_service import create_user, list_users, update_user, delete_user_by_id, get_user_by_id

users_bp = Blueprint("users", __name__)

@users_bp.get("/users")
def get_users():
    users = list_users()
    return jsonify([{"id": user.id, "name": user.name} for user in users])

@users_bp.get("/users/<int:user_id>")
def get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "user not found"}), 404
    return jsonify({"id": user.id, "name": user.name})

@users_bp.post("/users")
def post_user():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    if not name:
        return jsonify({"error": "name is required"}), 400

    user = create_user(name)
    return jsonify({"id": user.id, "name": user.name}), 201

@users_bp.put("/users/<int:user_id>")
def put_user(user_id):
    data = request.get_json(silent=True) or {}
    new_name = (data.get("name") or "").strip()

    if not new_name:
        return jsonify({"error": "new name is not found"}), 400

    user = update_user(user_id, new_name)

    if not user:
        return jsonify({"error": "user not found"}), 404
    return jsonify({"id": user.id, "name": user.name}), 200

@users_bp.delete("/users/<int:user_id>")
def delete_user(user_id):
    ok = delete_user_by_id(user_id)

    if not ok:
        return jsonify({"error": "user not found"}), 404
    return jsonify({"status": "ok"}), 200

