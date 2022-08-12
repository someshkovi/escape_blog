from django import forms
from tutorials.models import Tutorial, TutorialTopic

from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class TutorialForm(forms.ModelForm):
    slug = forms.CharField(help_text='Create a custom slug if required. Will be auto created if not provided', required=False)
    class Meta:
        model = Tutorial
        fields = ['title','slug']

class TutorialTopicForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )
    # slug = forms.CharField(label='Sluggified name')

    class Meta:
        model = TutorialTopic
        fields = ['topic_title','topic_sub_title',
          'content',
        #    'slug',
            'previous_topic', 'next_topic']