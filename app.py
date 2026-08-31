from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/api/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    name = data.get("name")
    email = data.get("email")
    plan = data.get("plan")

    # New backend feature:
    # "plan" is now required.
    if not name:
        return jsonify({
            "error": "name is required"
        }), 400

    if not email:
        return jsonify({
            "error": "email is required"
        }), 400

    if not plan:
        return jsonify({
            "error": "plan is required"
        }), 400

    return jsonify({
        "message": "User created successfully",
        "user": {
            "name": name,
            "email": email,
            "plan": plan
        }
    }), 201


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )