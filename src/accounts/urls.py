from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView, LoginView

from accounts.views import SettingsView, DisplayListView, SettingsFormView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('accounts:login')), name='logout'),
    # path('displays/<int:pk>', DisplayListView.as_view(), name='display'),
    path('settings/<int:pk>', SettingsFormView.as_view(), name='settings'),
    path('', DisplayListView.as_view(), name='displays')
]
