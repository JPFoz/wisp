from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "Home"


@app.route('/wind_speeds')
def get_wind_speed():
    return jsonify(results=[
    {
      "date_created": "Sun, 30 Jun 2019 21:36:31 GMT",
      "wind_speed": 5.9
    },
    {
      "date_created": "Sun, 30 Jun 2019 21:36:36 GMT",
      "wind_speed": 4.2
    },
    {
      "date_created": "Sun, 30 Jun 2019 21:36:41 GMT",
      "wind_speed": 2.8
    }])

@app.route('/passive_measurements')
def get_passive_measurements():
    return jsonify(results=[
    {
      "date_created": "Sun, 30 Jun 2019 21:36:31 GMT",
      "temperature": 5.9,
      "humidity": 67,
      "pressure": 1018
    },
    {
      "date_created": "Sun, 30 Jun 2019 21:36:36 GMT",
      "wind_speed": 4.2,
      "temperature": 1.0,
      "humidity": 55,
      "pressure": 1010
    },
    {
      "date_created": "Sun, 30 Jun 2019 21:36:41 GMT",
      "temperature": 8.9,
      "humidity": 90,
      "pressure": 1102
    }])


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
