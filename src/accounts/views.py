from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView, ListView, DetailView, UpdateView

from accounts.models import Customer
from accounts.forms import SettingsForm
from topics.models import Topic
from displays.models import MyDisplayModel, Display


class LoginView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/login.html'


class DisplayListView(LoginRequiredMixin, ListView):
    model = Display

    template_name = 'accounts/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data
    #     return context

    def get_queryset(self):
        return self.model.objects.filter(customer=self.request.user.customer)


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/settings.html'

    success_url = '/accounts/settings/'

    # display = MyDisplayModel.objects.get(pk=1)
    # lines = display.lines.all()

    topics = Topic.objects.all()

    def get_context_data(self, **kwargs):
        display = MyDisplayModel.objects.get(display__serial_number=self.kwargs['serial_number'])
        context = {
            'display_properties': '',
            'topics': '',
            'display': display
        }
        return context

    # display = MyDisplayModel.objects.get(pk=1)
    # display_lines = display.lines.count()
    # for lines in display:
    #     print(lines)


class SettingsFormView(LoginRequiredMixin, UpdateView):
    model = Display
    template_name = 'accounts/settings.html'
    form_class = SettingsForm

    def get_maxlines(self, customer):
        print(customer)
        return {"": ""}

    # def get_context_data(self, **kwargs):
    #
    #     lines = []
    #     display_pk = self.kwargs['pk']
    #     customer = Customer.objects.get(display__pk=display_pk)
    #     display = customer.display.get(pk=display_pk)
    #
    #     # x = customer.display.get(serial_number=display.serial_number)
    #     for line in display.lines.all():
    #         lines.append(line)
    #     # context = super(SettingsFormView, self).get_context_data(**kwargs)
    #     # context['customer'] = customer
    #     # context['display'] = display
    #     # context['topics'] = Topic.objects.all()
    #     # context['lines'] = lines
    #     # context['display_model'] = MyDisplayModel.objects.get(display__pk=self.kwargs['pk'])
    #     # context['pollo'] = 'pollo'
    #     # y= customer.display.get()
    #     # print(y.all())
    #     return {}

    def get_success_url(self):
        return '/accounts/settings/{}'.format(self.kwargs.get('pk'))

    def form_valid(self, form):
        x=SettingsForm(self.request)
        print(form.cleaned_data)
        print('valid')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(self.kwargs)
        # print(self.form)
        print('invalid')
        return super().form_invalid(form)
