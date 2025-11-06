from flask import Flask, request, jsonify
import joblib
import numpy as np
import traceback

app = Flask(__name__)

# -------------------------------
# Load model
# -------------------------------
try:
    model_obj = joblib.load("pipeline.pkl")

    # Handle both direct model and dict-wrapped models
    if isinstance(model_obj, dict):
        model = model_obj.get("model", None)
        print("ℹ️ Loaded model from dictionary structure.")
    else:
        model = model_obj

    if model is not None:
        print("✅ Model loaded successfully.")
        MODEL_LOADED = True
    else:
        print("❌ No model found in pipeline.pkl")
        MODEL_LOADED = False

except Exception as e:
    print("❌ Error loading model:", e)
    MODEL_LOADED = False


# -------------------------------
# Routes
# -------------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Predictive Model API! Use POST /predict to get predictions."
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok" if MODEL_LOADED else "model load failed",
        "model_loaded": MODEL_LOADED
    })


@app.route("/predict", methods=["POST"])
def predict():
    if not MODEL_LOADED:
        return jsonify({"error": "Model not loaded on server"}), 500

    try:
        data = request.get_json(force=True)
        if not data or "input" not in data:
            return jsonify({"error": "Missing 'input' in request body"}), 400

        input_data = data["input"]

        if not isinstance(input_data, dict):
            return jsonify({"error": "Invalid input format. Expected a JSON object with features."}), 400

        # Convert values to numeric array
        try:
            features = np.array(list(input_data.values()),
                                dtype=float).reshape(1, -1)
        except Exception as parse_err:
            return jsonify({"error": f"Failed to parse numeric input: {parse_err}"}), 400

        # Use correct model object for prediction
        preds = model.predict(features).tolist()

        return jsonify({
            "n": len(preds),
            "predictions": preds
        }), 200

    except Exception as e:
        print("❌ Internal error:", traceback.format_exc())
        return jsonify({
            "error": "Internal Server Error",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
