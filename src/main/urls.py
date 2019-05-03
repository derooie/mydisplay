from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display/', include('displays.urls', namespace='display')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
