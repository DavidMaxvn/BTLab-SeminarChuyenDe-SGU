from flask import Flask, jsonify, request
import pandas as pd

from src.manhattan import get_manhattan_distance

app = Flask(__name__)


def _parse_dataframe_payload(payload):
    if not isinstance(payload, dict):
        raise ValueError("df1/df2 phải là object JSON chứa data/index/columns")

    required = ["data", "index", "columns"]
    for key in required:
        if key not in payload:
            raise KeyError(f"Thiếu khóa '{key}' cho DataFrame")

    return pd.DataFrame(
        data=payload["data"],
        index=payload["index"],
        columns=payload["columns"],
    )


@app.route("/manhattan", methods=["POST"])
def calculate_manhattan():
    try:
        payload = request.get_json(force=True)
        if not payload or "df1" not in payload or "df2" not in payload:
            raise ValueError("Yêu cầu phải chứa df1 và df2")

        df1 = _parse_dataframe_payload(payload["df1"])
        df2 = _parse_dataframe_payload(payload["df2"])

        distance = get_manhattan_distance(df1, df2)

        return jsonify({"distance": float(distance)})

    except (ValueError, KeyError, TypeError) as err:
        return jsonify({"error": str(err)}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5000)