from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from django.views.generic.edit import FormView

from accounts.forms import SettingsForm


class LoginView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/login.html'


class SettingsView(LoginRequiredMixin, FormView):

    form_class = SettingsForm
    success_url = '/accounts/settings'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

