from flask import Flask, request, jsonify
from tasks import log_response
app = Flask(__name__)

@app.route("/", methods=["GET"])
def root_status():
    return jsonify({"status": "✅ Flask server is running"}), 200


import logging

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

# Console handler (stdout)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(console_handler)
@app.route("/doku/payment-notification", methods=["POST"])
def doku_notification():
    data = request.get_json(force=True)  # Parse JSON body
    # log_response.delay(data)
    logger.info(data)
    print("📩 Received DOKU Notification:")
    # print(data)

    # Respond with HTTP 200 and confirmation message
    return jsonify({"message": "Notification received"}), 200

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
