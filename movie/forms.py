from django.forms import ModelForm

from movie.models import FeedBack


class FeedBackForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = ('feedback',)
