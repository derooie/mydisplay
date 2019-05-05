from django.forms import ModelForm, ModelChoiceField, Form, Select, Textarea, ChoiceField, ModelMultipleChoiceField, \
    RadioSelect, inlineformset_factory, TextInput

from topics.models import Topic
from displays.models import Line, MyDisplayModel, Display

from accounts.models import Customer


class DisplayForm(ModelForm):
    class Meta:
        model = Display
        exclude = ('id', )


class LineForm(ModelForm):
    class Meta:
        model = Line
        exclude = ('id', )

        widgets = {
            'line': TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'user_text': TextInput(attrs={'class': 'form-control'}),
            'topic': Select(attrs={'class': 'form-control'}),
        }


DisplayLineFormSet = inlineformset_factory(Display, Line, form=LineForm, extra=0)
