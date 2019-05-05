from rest_framework import serializers

from displays.models import Display


class DisplaySerializer(serializers.Serializer):
    serial_number = serializers.IntegerField()
    friendly_name = serializers.CharField(max_length=64)


class LineSerializer(serializers.Serializer):
    line = serializers.CharField(max_length=16)
    user_text = serializers.CharField(max_length=16)
    topic = serializers.CharField()
