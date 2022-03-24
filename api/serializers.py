from rest_framework import serializers
from core.models import SensorReading


class SensorReadingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorReading
        fields = '__all__'
