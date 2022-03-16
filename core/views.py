import json

from django.views import generic
from core.models import SensorReading
from core.tools.helpers import JsonEncoder


class BaseIndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(BaseIndexView, self).get_context_data(**kwargs)

        sensor_reading = SensorReading.objects.filter(setting__id=1).values_list(
            'working_duration', 'number_of_telemetry_packets', 'battery_voltage', 'altitude',
            'velocity', 'no2_level_in_ppm', 'co_level_in_ppm', 'h2_level_in_ppm', 'latitude', 'longitude',
            'has_recording_started'
        )[0]
        labels = [field.name for field in SensorReading._meta.fields
                  if field.name not in ['id', 'setting', 'created_at', 'updated_at', 'departure_time']]

        context['dataset'] = json.dumps(sensor_reading)
        context['labels'] = json.dumps(labels)

        return context
