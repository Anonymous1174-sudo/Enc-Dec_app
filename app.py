from flask import Flask, render_template, request, jsonify
import base64
import os
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate or load an encryption key
KEY_FILE = "secret.key"

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        return key

key = load_key()
cipher = Fernet(key)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.json["data"]
    method = request.json["method"]

    if method == "aes":
        encrypted_data = cipher.encrypt(data.encode()).decode()
    elif method == "base64":
        encrypted_data = base64.b64encode(data.encode()).decode()
    else:
        return jsonify({"error": "Invalid encryption method"}), 400

    return jsonify({"result": encrypted_data})

@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.json["data"]
    method = request.json["method"]

    try:
        if method == "aes":
            decrypted_data = cipher.decrypt(data.encode()).decode()
        elif method == "base64":
            decrypted_data = base64.b64decode(data.encode()).decode()
        else:
            return jsonify({"error": "Invalid decryption method"}), 400
    except Exception:
        return jsonify({"error": "Decryption failed"}), 400

    return jsonify({"result": decrypted_data})

if __name__ == "__main__":
    app.run(debug=True)
