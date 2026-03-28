"""Flask API example for Chapter 12."""

from __future__ import annotations

from flask import Flask, jsonify, request

from .utils import calculate_distance_from_payload

app = Flask(__name__)


@app.route("/distances", methods=["POST"])
def calculate_distance():
    """Calculate distance between two vectors from a POST request."""
    try:
        payload = request.get_json(force=True)
        result = calculate_distance_from_payload(payload)
        return jsonify({"distance": result})
    except Exception as exc:  # pragma: no cover - simple API example
        return jsonify({"error": str(exc)}), 400


if __name__ == "__main__":  # pragma: no cover
    app.run(debug=True)
