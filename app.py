from flask import Flask, request, jsonify
from tasks import log_response
app = Flask(__name__)

@app.route("/", methods=["GET"])
def root_status():
    return jsonify({"status": "✅ Flask server is running"}), 200


@app.route("/doku/payment-notification", methods=["POST"])
def doku_notification():
    data = request.get_json(force=True)  # Parse JSON body
    log_response.delay(data)
    print("📩 Received DOKU Notification:")
    print(data)

    # Respond with HTTP 200 and confirmation message
    return jsonify({"message": "Notification received"}), 200

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
