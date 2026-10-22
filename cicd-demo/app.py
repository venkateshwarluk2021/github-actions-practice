from flask import Flask, jsonify
app = Flask(__name__)
VERSION = "1.0.0"


@app.get("/")
def home():
    return jsonify(message="Hello from CI/CD pipeline!", version=VERSION)


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
