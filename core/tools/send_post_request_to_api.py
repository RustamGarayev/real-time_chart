import time
import requests

from random import randint, uniform
from datetime import datetime

url = 'http://127.0.0.1:8000/api/v1/sensor-reading-create/'

for i in range(60):
    payload = {
        'setting': 1,
        'working_duration': i + 1,
        'number_of_telemetry_packets': i + 1,
        "battery_voltage": round(uniform(5.5, 6.1), 2),
        "altitude": round(uniform(2.5, 3.0), 2),
        "distance_to_ground": round(uniform(10.0, 12.0), 2),
        "velocity": round(uniform(1113, 1119), 2),
        "temperature": round(uniform(23, 25), 2),
        "no2_level_in_ppm": round(uniform(40, 42), 2),
        "co_level_in_ppm": round(uniform(60, 61), 2),
        "h2_level_in_ppm": round(uniform(3, 4), 2),
        "gps_latitude": 40.4093,
        "gps_longitude": 49.8671,
        "gps_altitude": -28.0,
        "has_recording_started": True,
        "departure_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
    }

    try:
        response = requests.post(url, json=payload)
        print(response.status_code)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(e)

    time.sleep(1)


# def send_post_request_to_api(url, payload):
#     try:
#         response = requests.post(url, json=payload)
#         print(response.status_code)
#         print(response.text)
#     except requests.exceptions.RequestException as e:
#         print(e)
