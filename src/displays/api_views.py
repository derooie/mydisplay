from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
import json
from displays.models import Line
from displays.serializers import LineSerializer

app_name = 'displays'


class DisplayDetailAPIView(GenericAPIView):
    # serializer_class = LineSerializer

    def get(self, request, serial_number):
        obj = Line.objects.filter(display__serial_number=serial_number)
        lines = {}
        for item in obj:
            lines[item.line] = {
                "topic": item.topic.topic.lower(),
                "user_text": item.user_text
            }
        print(lines)
        return Response(lines)
