from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return "Weather Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    temperature = data["temperature"]
    humidity = data["humidity"]

    prediction = model.predict([[temperature, humidity]])

    return jsonify({
        "predicted_temperature": round(float(prediction[0]), 2)
    })

if __name__ == "__main__":
 if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)