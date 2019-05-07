
from rest_framework.authentication import BasicAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.db import IntegrityError
from rest_framework.views import APIView

from displays.models import Line, Display, MyDisplayModel
from displays.serializers import DisplaySerializer

app_name = 'displays'


class DisplayDetailAPIView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, serial_number):
        obj = Line.objects.filter(display__serial_number=serial_number)
        lines = {}
        for item in obj:
            lines[item.line] = {
                "topic": item.topic.topic.lower(),
                "user_text": item.user_text
            }
        return Response(lines)

    def post(self, request):
        serializer = DisplaySerializer(data=request.data)
        try:
            if serializer.is_valid():
                display = Display.objects.create(
                    serial_number=serializer.data['serial_number'],
                    model=MyDisplayModel.objects.get(pk=serializer.data['display_model'])
                )
            else:
                return Response({"error": "Provided data is invalid"})
        except IntegrityError:
            return Response({"error": "Serial already exists"})
        return Response({"Created display with serial number": display.serial_number})
