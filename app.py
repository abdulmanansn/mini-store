
from flask import Flask, request, jsonify, send_from_directory
import sqlite3

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect("store.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/style.css")
def css():
    return send_from_directory(".", "style.css")

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    try:
        conn = sqlite3.connect("store.db")
        conn.execute(
            "INSERT INTO customers (name, email) VALUES (?, ?)",
            (data["name"], data["email"])
        )
        conn.commit()
        conn.close()

        return jsonify({"message": "Customer registered!"})

    except sqlite3.IntegrityError:
        return jsonify({"message": "Email already registered!"}), 409

create_database()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
