
from flask import Flask, jsonify
from datetime import datetime
import logging

app = Flask(__name__)

# Save application logs to a file
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

@app.route("/")
def home():
    app.logger.info("Home endpoint accessed")
    return jsonify({
        "application": "Mini Status App",
        "message": "Application is running!"
    })

@app.route("/health")
def health():
    app.logger.info("Health check successful")
    return jsonify({
        "application": "Mini Status App",
        "status": "UP",
        "timestamp": datetime.now().isoformat()
    })

@app.errorhandler(404)
def not_found(error):
    app.logger.warning("404 Not Found: %s", error)
    return jsonify({"error": "Endpoint not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
