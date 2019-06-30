from flask import Flask, request
from utils.db_accessor import DbAccessor

app = Flask(__name__)
db_accessor = DbAccessor()


@app.route('/')
def home():
    return "Home"


@app.route('/passive_measurements')
def get_passive_measurements():
    dates = get_date_params(request)
    return db_accessor.get_passive_measurement_data(dates[0], dates[1])


@app.route('/wind_speed')
def get_wind_speed():
    dates = get_date_params(request)
    return db_accessor.get_wind_speed_measurements(dates[0], dates[1])


@app.route('/wind_gusts')
def get_wind_gusts():
    dates = get_date_params(request)
    return db_accessor.get_wind_gust_measurement(dates[0], dates[1])


def get_date_params(client_request):
    return client_request.args.get('date_start'), client_request.args.get('date_end')


if __name__ == '__main__':
    app.run()
