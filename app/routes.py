from flask import Blueprint, jsonify
from app.services.user_service import UserService
from app.utils.errors import APIError, ExternalAPIError

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/users", methods=["GET"])
def get_users():
    """Endpoint to return 75 randomly generated users"""
    try:
        users = UserService.get_random_users()
        return jsonify(users)
    except ExternalAPIError as e:
        return jsonify({"error": e.message}), e.status_code
    except APIError as e:
        return jsonify({"error": e.message}), e.status_code
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Main route
@api_bp.route("/", methods=["GET"])
def home():
    return jsonify(
        {"message": "Flask API for Random Users", "endpoints": {"users": "/api/users"}}
    )
