from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from app.utils.errors import APIError


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Enable CORS
    CORS(app)

    # Register error handlers
    @app.errorhandler(APIError)
    def handle_api_error(error):
        return jsonify({"error": error.message}), error.status_code

    @app.errorhandler(404)
    def handle_not_found(error):
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(500)
    def handle_server_error(error):
        return jsonify({"error": "Internal server error"}), 500

    # Register routes
    from app.routes import api_bp

    app.register_blueprint(api_bp)

    return app
