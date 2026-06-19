from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():

    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])

    prediction = model.predict([[temperature, humidity]])

    predicted_temp = round(float(prediction[0]), 2)

    if predicted_temp > 35:
        weather_status = "🔥 Hot"
    elif predicted_temp > 25:
        weather_status = "🌤 Pleasant"
    else:
        weather_status = "❄ Cool"

    return render_template(
        "index.html",
        prediction=predicted_temp,
        temp=temperature,
        humidity=humidity,
        weather_status=weather_status
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)