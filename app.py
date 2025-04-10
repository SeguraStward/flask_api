from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
# RandomUser.me API URL
API_URL = "https://randomuser.me/api/"


# Endpoint to return generated users
@app.route("/api/users", methods=["GET"])
def get_users():
    try:
        # Make a request to get 75 random users from the API
        response = requests.get(API_URL, params={"results": 75})
        response.raise_for_status()  # Raises an exception if there is an error

        # Get user data
        users_data = response.json()["results"]

        # Return users as a JSON response
        return jsonify(users_data)
    except Exception as e:
        # If there's an error, return an error message
        return jsonify({"error": str(e)}), 500


# Default route
@app.route("/")
def home():
    return "Flask API for Random Users"


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
