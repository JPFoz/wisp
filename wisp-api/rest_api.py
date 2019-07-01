from flask import Flask, request, jsonify
import datetime
from datetime import timedelta
from utils.db_accessor import DbAccessor

app = Flask(__name__)
db_accessor = DbAccessor()


@app.route('/')
def home():
    return "Home"


@app.route('/passive_measurements')
def get_passive_measurements():
    dates = get_date_params(request)
    return jsonify(results=db_accessor.get_passive_measurement_data(dates[0], dates[1]))


@app.route('/wind_speeds')
def get_wind_speed():
    dates = get_date_params(request)
    return jsonify(results=db_accessor.get_wind_speed_measurements(dates[0], dates[1]))


@app.route('/wind_gusts')
def get_wind_gusts():
    dates = get_date_params(request)
    return jsonify(results=db_accessor.get_wind_gust_measurement(dates[0], dates[1]))


def get_date_params(client_request):
    date_start = client_request.args.get('date_start')
    date_end = client_request.args.get('date_end')

    if not date_start:
        date_start_datetime = datetime.datetime.now() - timedelta(hours=6)
    else:
        date_start_datetime = datetime.datetime.strptime(date_start, '%Y-%m-%d %H:%M:%S.%f')

    if not date_end:
        date_end_datetime = datetime.datetime.now()
    else:
        date_end_datetime = datetime.datetime.strptime(date_end, '%Y-%m-%d %H:%M:%S.%f')

    return date_start_datetime, date_end_datetime


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
