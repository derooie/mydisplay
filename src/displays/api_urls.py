from django.urls import path
from rest_framework import routers

from displays.api_views import DisplayDetailAPIView

router = routers.DefaultRouter()


urlpatterns = [
    path('get_serial/<int:serial_number>', DisplayDetailAPIView.as_view()),
]
