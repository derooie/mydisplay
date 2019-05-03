from rest_framework.generics import ListAPIView

from displays.models import Line
from displays.serializers import LineSerializer

app_name = 'displays'


class DisplayDetailAPIView(ListAPIView):
    serializer_class = LineSerializer

    def get_queryset(self):
        return Line.objects.filter(display__serial_number=self.kwargs['serial_number'])
