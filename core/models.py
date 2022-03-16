from django.db import models


class Setting(models.Model):
    team_id = models.PositiveIntegerField()

    website_title = models.CharField(max_length=50, default="Cansat - Teknofest", blank=True)

    def __str__(self):
        return self.website_title


class SensorReading(models.Model):
    setting = models.ForeignKey('Setting', on_delete=models.PROTECT, related_name='sensor_readings')

    working_duration = models.PositiveIntegerField(default=0, blank=True)
    number_of_telemetry_packets = models.PositiveIntegerField(default=0, blank=True)
    battery_voltage = models.FloatField(default=0.0, blank=True)
    altitude = models.FloatField(default=0.0, blank=True)
    velocity = models.FloatField(default=0.0, blank=True)

    no2_level_in_ppm = models.FloatField(default=0.0, blank=True)
    co_level_in_ppm = models.FloatField(default=0.0, blank=True)
    h2_level_in_ppm = models.FloatField(default=0.0, blank=True)

    latitude = models.FloatField(default=0.0, blank=True)
    longitude = models.FloatField(default=0.0, blank=True)

    has_recording_started = models.BooleanField(default=False, blank=True)
    departure_time = models.DateTimeField(null=True)

    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Sensor Readings'
        ordering = ('-created_at',)

    def __str__(self):
        return "%s %s" % (str(self.setting.team_id), str(self.number_of_telemetry_packets))
