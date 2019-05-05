from rest_framework import serializers
from rest_framework.response import Response

from displays.models import Line


class DisplaySerializer(serializers.Serializer):
    serial_number = serializers.IntegerField()
    friendly_name = serializers.CharField(max_length=64)


class Pollo(serializers.Serializer):
    line = serializers.PrimaryKeyRelatedField(queryset=Line.objects.get(pk=1))
    topic = serializers.CharField()
    # user_text = serializers.CharField()


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = ('line', 'user_text', 'topic',)


    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['topic'] = ret['topic'].lower()
    #     return ret
    #
    # def list(self, request, *args, **kwargs):
    #     self.object_list = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(self.object_list, many=True)
    #     return Response({'results': serializer.data})
