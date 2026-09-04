from flask import Flask, request, jsonify, send_from_directory
import hashlib
import os

app = Flask(**name**)

VERIFICATION_TOKEN = os.environ.get("EBAY_VERIFICATION_TOKEN", "")

ENDPOINT_URL = "https://ebay-notification-endpoint-eagf.onrender.com/ebay/notification"

@app.route("/ebay/notification", methods=["GET", "POST"])
def ebay_notification():
challenge_code = request.args.get("challenge_code")

```
if challenge_code:
    response_hash = hashlib.sha256(
        (
            challenge_code
            + VERIFICATION_TOKEN
            + ENDPOINT_URL
        ).encode("utf-8")
    ).hexdigest()

    return jsonify({
        "challengeResponse": response_hash
    }), 200

return jsonify({
    "status": "OK"
}), 200
```

@app.route("/", methods=["GET"])
def home():
return "eBay notification endpoint is running."

@app.route("/privacy-policy", methods=["GET"])
def privacy_policy():
return send_from_directory(
os.path.dirname(os.path.abspath(**file**)),
"privacy_policy.html"
)

if **name** == "**main**":
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
