from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import requests
from io import BytesIO
from inference_sdk import InferenceHTTPClient

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

EXTERNAL_API_URL = "https://classify.roboflow.com"
API_KEY = "1wZz1zRH0f4dghdwk80E"

@app.route('/upload', methods=['POST'])
def upload_image():
    image = request.files['image']  # DIRECT JPG/PNG IMAGE
    CLIENT = InferenceHTTPClient(
        api_url=EXTERNAL_API_URL,
        api_key=API_KEY,
    )

    result = CLIENT.infer(image, model_id="dog-breed-xpaq6/1")
    breed_name = result.get("top", None)  # This is now a string like 005.Alaskan_malamute

    return jsonify({"breed": breed_name})

if __name__ == '__main__':
    app.run(debug=True)
