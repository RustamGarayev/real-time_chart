import time
import requests

from random import randint
from datetime import datetime

url = 'http://127.0.0.1:8000/api/v1/sensor-reading-create/'

for i in range(60):
    payload = {
        'setting': 1,
        'working_duration': i + 1,
        'number_of_telemetry_packets': i + 1,
        "battery_voltage": randint(4, 6),
        "altitude": 60 - i,
        "velocity": randint(25, 30),
        "temperature": randint(24, 35),
        "n2_level_in_ppm": randint(90, 100),
        "co_level_in_ppm": randint(15, 20),
        "h2_level_in_ppm": randint(6, 10),
        "gps_latitude": 12.0,
        "gps_longitude": 23.0,
        "gps_altitude": 13.0,
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
