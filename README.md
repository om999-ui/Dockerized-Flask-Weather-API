# 🌤 Weather Prediction Web Application

A Machine Learning-powered Weather Prediction Web Application built using Flask, Scikit-Learn, Chart.js, and Docker.

## 🚀 Features

* Predicts weather temperature based on user inputs
* Interactive web interface using HTML and CSS
* Machine Learning model built with Scikit-Learn
* Real-time prediction results
* Weather status classification:

  * 🔥 Hot
  * 🌤 Pleasant
  * ❄ Cool
* Data visualization using Chart.js
* Dockerized application for easy deployment

## 🛠 Tech Stack

* Python
* Flask
* Scikit-Learn
* Joblib
* HTML5
* CSS3
* Chart.js
* Docker

## 📂 Project Structure

```text
WeatherMLAPI/
│
├── app.py
├── train_model.py
├── weather.csv
├── model.pkl
├── requirements.txt
├── Dockerfile
├── .dockerignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/om999-ui/Dockerized-Flask-Weather-API.git
cd Dockerized-Flask-Weather-API
```

### Create Virtual Environment

```bash
py -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
py app.py
```

Open:

```text
http://127.0.0.1:5000
```

## 🐳 Docker Setup

Build Docker Image:

```bash
docker build --network=host -t weather-api .
```

Run Container:

```bash
docker run -p 5000:5000 weather-api
```

## 📊 Machine Learning Workflow

1. Load weather dataset
2. Train Linear Regression model
3. Save model using Joblib
4. Load model in Flask application
5. Accept user input
6. Generate prediction
7. Display results and chart visualization

## 🎯 Future Improvements

* Live weather API integration
* Weather condition prediction
* Historical weather analysis
* Deployment on Render or AWS
* User authentication

## 👨‍💻 Author

**Om Masal**