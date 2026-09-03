from flask import Flask, request, Response
import hashlib
import os

app = Flask(__name__)

VERIFICATION_TOKEN = os.environ.get("EBAY_VERIFICATION_TOKEN", "")


@app.route("/ebay/notification", methods=["GET", "POST"])
def ebay_notification():
    challenge_code = request.args.get("challenge_code")

    if challenge_code:
        endpoint = request.url.split("?")[0]

        response_hash = hashlib.sha256(
            (challenge_code + VERIFICATION_TOKEN + endpoint).encode("utf-8")
        ).hexdigest()

        return Response(
            response_hash,
            status=200,
            mimetype="text/plain"
        )

    return Response("OK", status=200)


@app.route("/", methods=["GET"])
def home():
    return "eBay notification endpoint is running."


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
