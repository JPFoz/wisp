import bme280
import smbus2
import math
from time import sleep
from threading import Thread
from utils.db_accessor import DbAccessor
from gpiozero import Button

port = 1
address = 0x76
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus, address)
wind_speed_sensor = Button(5)
db_accessor = DbAccessor()

radius = 9  # cm
spin_count = 0
wind_speed_sample_duration = 5  # secs
wind_gust_sample_duration = 20  # secs
passive_sample_duration = 600  # secs
anemometer_factor = 1.18
cms_in_km = 100000.0
seconds_in_hour = 3600
wind_records = []


def make_passive_measurement():
    passive_measurement_data = bme280.sample(bus, address)
    humidity = passive_measurement_data.humidity
    pressure = passive_measurement_data.pressure
    ambient_temperature = passive_measurement_data.temperature
    db_accessor.insert_passive_measurement(temp=ambient_temperature,
                                           humidity=humidity,
                                           pressure=pressure)


def run_passive_daemon():
    while True:
        make_passive_measurement()
        sleep(passive_sample_duration)


def track_spin():
    global spin_count
    spin_count += 1


def calculate_wind_speed():
    rotations = spin_count / 2
    circumference = radius * (2 * math.pi)
    distance = ((rotations * circumference) / cms_in_km)
    wind_speed = (distance / wind_speed_sample_duration) * seconds_in_hour
    adjusted_wind_speed = wind_speed * anemometer_factor
    return adjusted_wind_speed


def run_active_wind_speed_daemon():
    global spin_count
    while True:
        spin_count = 0
        # wait proper duration
        sleep(wind_speed_sample_duration)
        # get speed
        wind_speed = calculate_wind_speed()
        # save to short term records used to get gusts
        wind_records.append(wind_speed)
        # save sample to the db
        db_accessor.insert_wind_speed_data(wind_speed)


def run_active_wind_gust_daemon():
    global wind_records
    while True:
        wind_records = []
        sleep(wind_gust_sample_duration)
        wind_gust = max(wind_records)
        db_accessor.insert_wind_gust_data(wind_gust)


def main():
    db_accessor.configure_connection()
    wind_speed_sensor.when_pressed = track_spin
    Thread(target=run_passive_daemon).start()
    Thread(target=run_active_wind_speed_daemon).start()
    Thread(target=run_active_wind_gust_daemon).start()


if __name__ == '__main__':
    main()

