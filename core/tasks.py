from __future__ import absolute_import, unicode_literals

import time
import RPi.GPIO as GPIO

from random import randint
from datetime import datetime

from chart_project.settings import TEAM_ID
from core.tools.send_post_request_to_api import send_post_request_to_api

# Pin defining and board mode
GPIO.setmode(GPIO.BOARD)
pin = 4
led = 13
buzzer = 23
GPIO.setup(led, GPIO.OUT)

altitude_change = 0


def start_reading_data():
    working_duration, number_of_telemetry_packets = 0, 0
    global altitude_change

    while True:
        # Sensor actions
        temperature, pressure, altitude = read_bmp280_data()
        gps_latitude, gps_longitude, gps_altitude = read_gps_data()
        voltage, current = read_im_data()
        no2, co, h2 = read_cjumc_data()

        working_duration += 1
        number_of_telemetry_packets += 1

        altitude_change = altitude - altitude_change

        # Video activation
        video_enabled = has_video_started()
        if video_enabled:
            activate_video()
            send_out_video()

        time.sleep(1)

        payload = {
            'team_id': TEAM_ID,
            'working_duration': working_duration,
            'number_of_telemetry_packets': number_of_telemetry_packets,
            'temperature': temperature,
            'pressure': pressure,
            'altitude': altitude,
            'gps_latitude': gps_latitude,
            'gps_longitude': gps_longitude,
            'gps_altitude': gps_altitude,
            'battery_voltage': voltage,
            'current': current,
            'velocity': randint(25, 30),  # TODO: fix this
            'no2_level_in_ppm': no2,
            'co_level_in_ppm': co,
            'h2_level_in_ppm': h2,
            'has_recording_started': has_video_started(),
            'departure_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") if video_enabled else None,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
        }

        # Send data to API
        send_post_request_to_api('http://127.0.0.1:8000/api/v1/sensor-reading-create/', payload)

        # Sensor reached to the ground
        if altitude < 1:
            # Activate the buzzer
            GPIO.output(buzzer, GPIO.HIGH)
            break


def read_bmp280_data():
    temperature = bmp280.temperature
    pressure = bmp280.pressure
    altitude = bmp280.altitude

    return temperature, pressure, altitude


def read_gps_data():
    return lat, long, alt


def read_im_data():
    return voltage, current


def read_cjumc_data():
    return no2, co, h2


def activate_video():
    return


def send_out_video():
    return


def has_video_started():
    # Check whether altitude change is negative, if so, video should be started
    if altitude_change < 0:
        return True
    return False
