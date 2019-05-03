from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, FormView, UpdateView

from displays.models import Topic
from displays.forms import LineChoiceForm


def add_line(request):
    print('Added a line')
    return HttpResponse("You're voting on questio")


class AddLineView(UpdateView):
    model = Topic
    form_class = LineChoiceForm
    template_name = 'displays/line_choice.html'
    success_url = '/display/2'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        print(form)
        return super().form_valid(form)
