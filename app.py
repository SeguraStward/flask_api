from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
# URL de la API RandomUser.me
API_URL = "https://randomuser.me/api/"

# Endpoint para devolver los usuarios generados
@app.route("/api/users", methods=["GET"])
def get_users():
    try:
        # Realizar solicitud para obtener 75 usuarios aleatorios de la API
        response = requests.get(API_URL, params={"results": 75})
        response.raise_for_status()  # Lanza una excepción si hay un error

        # Obtener los datos de los usuarios
        users_data = response.json()["results"]
        
        # Devolver los usuarios como respuesta JSON
        return jsonify(users_data)
    except Exception as e:
        # Si hay un error, devolver un mensaje de error
        return jsonify({"error": str(e)}), 500

# Ruta por defecto
@app.route('/')
def home():
    return "Flask API for Random Users"

if __name__ == "__main__":
    # Ejecutar la aplicación Flask
    app.run(debug=True)
