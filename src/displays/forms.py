from django.forms import ModelForm, ModelChoiceField, Form, Select, Textarea, ChoiceField, ModelMultipleChoiceField, \
    RadioSelect

from displays.models import Line, MyDisplayModel, Display

TEXT_WIDGET = {'cols': 20, 'rows': 5, 'class': 'form-control'}
SELECT_WIDGET = {'class': 'form-control'}


class LineChoiceForm(ModelForm):
    # topics = Topic.objects.all()
    #

    class Meta:
        model = Line
        exclude = ('id', )

        widgets = {
            'topic': Select(attrs=SELECT_WIDGET),
            # 'lines': Select()

        }

    # print(display)
    # for line in display.lines.all():
    #     print(line)
