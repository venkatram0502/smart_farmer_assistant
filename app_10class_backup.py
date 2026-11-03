from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "success": True,
        "message": "Smart Farmer AI Backend is running"
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "file" not in request.files:
            return jsonify({
                "success": False,
                "message": "No image file received"
            }), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({
                "success": False,
                "message": "No image selected"
            }), 400

        # Verify that the uploaded file is a valid image
        image_data = file.read()
        image = Image.open(io.BytesIO(image_data))
        image.verify()

        print(f"Received image: {file.filename}")

        # Temporary prediction until trained model is connected
        return jsonify({
            "success": True,
            "prediction": "Healthy",
            "confidence": 0.92,
            "message": "Image received successfully"
        })

    except Exception as e:
        print(f"Prediction error: {e}")

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


if __name__ == "__main__":
    print("========================================")
    print(" Smart Farmer AI Backend")
    print("========================================")
    print("Server: http://10.0.2.2:5000")
    print("Predict: http://10.0.2.2:5000/predict")
    print("========================================")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )