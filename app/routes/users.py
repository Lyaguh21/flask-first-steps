from flask import Blueprint, request, jsonify
from ..services.user_service import create_user, list_users

users_bp = Blueprint("users", __name__)

@users_bp.get("/users")
def get_users():
    users = list_users()
    return jsonify([{"id": u.id, "name": u.name} for u in users])

@users_bp.post("/users")
def post_user():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    if not name:
        return jsonify({"error": "name is required"}), 400

    user = create_user(name)
    return jsonify({"id": user.id, "name": user.name}), 201
