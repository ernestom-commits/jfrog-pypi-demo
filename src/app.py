from flask import Flask, jsonify
import yaml
import requests

app = Flask(__name__)

CATALOG = [
    {"id": 1, "title": "Spring4Shell", "type": "vulnerability", "severity": "critical"},
    {"id": 2, "title": "Log4Shell",    "type": "vulnerability", "severity": "critical"},
    {"id": 3, "title": "Text4Shell",   "type": "vulnerability", "severity": "high"},
]

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/catalog")
def catalog():
    return jsonify(CATALOG)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
