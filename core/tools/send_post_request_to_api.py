import time
import requests

from random import randint

url = 'http://127.0.0.1:8000/api/v1/sensor-reading-create/'

for i in range(15):
    payload = {
        'setting': 1,
        'working_duration': i + 1,
        'number_of_telemetry_packets': i*3,
        "battery_voltage": randint(4, 6),
        "altitude": randint(2, 60),
        "velocity": randint(20, 30),
        "no2_level_in_ppm": randint(0, 100),
        "co_level_in_ppm": randint(0, 20),
        "h2_level_in_ppm": randint(0, 10),
        "latitude": 12.0,
        "longitude": 23.0,
        "has_recording_started": True,
        "departure_time": f"2022-03-16T11:2{i}:00+04:00",
        "created_at": f"2022-03-16T11:22:27.906146{i}+04:00",
        "updated_at": f"2022-03-16T11:22:27.906167{i}+04:00",
    }

    try:
        response = requests.post(url, json=payload)
        print(response.status_code)
    except requests.exceptions.RequestException as e:
        print(e)

    time.sleep(1)
