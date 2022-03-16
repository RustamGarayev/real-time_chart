from django.contrib import admin
from core.models import *


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    pass


@admin.register(SensorReading)
class SensorReadingAdmin(admin.ModelAdmin):
    pass
