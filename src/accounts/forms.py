from django.forms import ModelForm, ModelChoiceField

from accounts.models import Topic


class SettingsForm(ModelForm):
    class Meta:
        model = Topic
        fields = ('topic',)

    topic = ModelChoiceField(queryset=Topic.objects.all())




