from django.forms import ModelForm, ModelChoiceField, Form, Select, Textarea, ChoiceField, ModelMultipleChoiceField, \
    RadioSelect, inlineformset_factory

from topics.models import Topic
from displays.models import Line, MyDisplayModel, Display

from accounts.models import Customer


class DisplayForm(ModelForm):
    class Meta:
        model = Display
        exclude = ('id', 'model' )


class LineForm(ModelForm):
    class Meta:
        model = Line
        exclude = ('id', 'model')


DisplayLineFormSet = inlineformset_factory(Display, Line, form=LineForm, extra=0)
