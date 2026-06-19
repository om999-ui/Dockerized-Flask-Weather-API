import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv("weather.csv")

X = data[["temperature", "humidity"]]
y = data["next_day_temp"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model Trained Successfully!")