from django.forms import ModelForm, ModelChoiceField, Form, Select, Textarea, ChoiceField, ModelMultipleChoiceField, \
    RadioSelect

from topics.models import Topic
from displays.models import Line, MyDisplayModel, Display

from accounts.models import Customer

TEXT_WIDGET = {'cols': 20, 'rows': 5, 'class': 'form-control'}
SELECT_WIDGET = {'class': 'form-control'}


class SettingsForm(ModelForm):
    topics = Topic.objects.all()
    #

    class Meta:
        model = Display
        exclude = ('id', 'model', 'serial_number')

        widgets = {
            'topic': Select(attrs=SELECT_WIDGET),
            # 'lines': Select()

        }

    # print(display)
    # for line in display.lines.all():
    #     print(line)
