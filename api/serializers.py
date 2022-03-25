from rest_framework import serializers
from core.models import SensorReading


class SensorReadingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorReading
        fields = '__all__'

    # def create(self, validated_data):
    #     """
    #     Create and return a new `SensorReading` instance, given the validated data.
    #         :param validated_data:
    #         :return:
    #     """
    #     return SensorReading.objects.create(**validated_data)
