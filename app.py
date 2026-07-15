from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "SaaS App is running!",
        "time": str(datetime.datetime.now())
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200