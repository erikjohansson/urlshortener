from django.forms import ModelForm
from shortener.models import Shorturl


class ShorturlForm(ModelForm):
    class Meta:
        model = Shorturl
        fields = ["url"]
        labels = {
            "url": "Add new URL",
        }
