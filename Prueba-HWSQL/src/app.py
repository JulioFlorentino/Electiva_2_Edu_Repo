from flask import Flask
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return "¡Hola Mundo! Conexión exitosa a MySQL 🎉"
    except Exception as e:
        return f"Error al conectar a MySQL: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
