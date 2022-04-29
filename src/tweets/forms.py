from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ['body'] # thumbnail tbd
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'What\'s happening?'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['thumbnail'].widget.attrs.update({'class':'custom-file-input'})