from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root_status():
    return jsonify({"status": "✅ Flask server is running"}), 200


@app.route("/doku/payment-notification", methods=["POST"])
def doku_notification():
    data = request.get_json(force=True)  # Parse JSON body
    print("📩 Received DOKU Notification:")
    print(data)

    # Respond with HTTP 200 and confirmation message
    return jsonify({"message": "Notification received"}), 200

if __name__ == "__main__":
    app.run(port=5000)
