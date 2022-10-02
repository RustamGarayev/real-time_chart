import json
import logging

from asyncio import sleep
from asgiref.sync import sync_to_async

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from core.models import SensorReading, Setting

site_setting = Setting.objects.first()

logging.basicConfig(level=logging.INFO)


class GraphConsumer(AsyncJsonWebsocketConsumer):

    @staticmethod
    @sync_to_async
    def __sensor_reading_to_json(sensor_reading):
        keys_to_remove = ('_state', 'id', 'departure_time', 'created_at', 'updated_at', 'has_recording_started')

        reading_as_dict = sensor_reading.__dict__

        # Remove unnecessary keys from dictionary
        for k in keys_to_remove:
            reading_as_dict.pop(k, None)

        return reading_as_dict

    @staticmethod
    @sync_to_async
    def get_sensor_data():
        return SensorReading.objects.first()

    def __sensor_readings_to_json(self, sensor_readings):
        return [self.__sensor_reading_to_json(sensor_reading) for sensor_reading in sensor_readings
                if sensor_reading is not None]

    async def fetch_sensor_readings(self):
        sensor_reading = SensorReading.objects.last()
        logging.info("Inside fetch sensor reading")
        context = {
            'sensor_reading': self.__sensor_reading_to_json(sensor_reading),
            'command': 'fetch_sensor_readings',
        }

        await self.send_data(context)

    async def connect(self):
        await self.accept()
        logging.info("Connected")

        # if site_setting.enable_sensor_reading:
        while True:
            sensor_reading = await self.get_sensor_data()
            logging.info("Inside fetch sensor reading")
            context = {
                'sensor_reading': await self.__sensor_reading_to_json(sensor_reading),
                'command': 'fetch_sensor_readings',
            }

            await self.send(json.dumps(context))
            await sleep(1)

    async def receive(self, text_data):
        data = json.loads(text_data)
        logging.info(data)
        return
        # self.fetch_sensor_readings()

    async def disconnect(self, close_code):
        pass

    async def send_data(self, sensor_data):
        await self.send(text_data=json.dumps(sensor_data))
