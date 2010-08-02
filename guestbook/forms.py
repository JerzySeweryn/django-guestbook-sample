from django.forms.models import ModelForm
from guestbook.models import Comments
from django.forms.widgets import Textarea, TextInput
from django import forms


class AddCommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('nickname', 'text')
        widgets = {
            'nickname': TextInput(attrs={'cols': 18, 'rows': 1, 'class':'textform'}),
            'text': Textarea(attrs={'cols': 80, 'rows': 5, 'class':'textform'}),
        }

class SearchForm(forms.Form):
    nickname = forms.CharField()
    widgets = {
            'nickname': TextInput(attrs={'cols': 18, 'rows': 1, 'class':'textform'}),
        }
