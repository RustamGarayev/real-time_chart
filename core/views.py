import csv
import logging

from django.views import generic
from django.http import HttpResponse

from core.models import Setting, SensorReading
from chart_project.settings import TEAM_ID

logging.basicConfig(level=logging.INFO)


class BaseIndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(BaseIndexView, self).get_context_data(**kwargs)

        context['team_id'] = Setting.objects.first().team_id

        return context


def export_sensor_data_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{TEAM_ID}_sensor_data.csv"'

    writer = csv.writer(response)

    not_included_fields = ['id', 'created_at', 'updated_at', 'setting']
    model_fields = ['TEAM ID'] + [field.name for field in SensorReading._meta.get_fields()
                                  if field.name not in not_included_fields]

    writer.writerow(model_fields)

    sensor_data = SensorReading.objects.all().order_by('id').values_list(
        'working_duration', 'number_of_telemetry_packets', 'battery_voltage', 'altitude', 'velocity', 'temperature',
        'no2_level_in_ppm', 'co_level_in_ppm', 'h2_level_in_ppm', 'gps_latitude', 'gps_longitude', 'gps_altitude',
        'has_recording_started', 'departure_time'
    )

    clean_sensor_data = map(lambda x: (TEAM_ID,) + x, sensor_data)

    for sensor_reading in clean_sensor_data:
        writer.writerow(sensor_reading)

    return response


# def start_sensor_reading(request):
#     if request.method == 'POST':
#         start_reading_data()
#
#         site_setting = Setting.objects.first()
#         site_setting.enable_sensor_reading = True
#         site_setting.save()
#
#         return HttpResponse('OK')
