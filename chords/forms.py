from django import forms
from .models import Song

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, required=False)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput, required=False)


class SongForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label='Title')

    body_w = forms.Textarea(attrs={'class': 'song_body song_body_edit', 'style': 'height: 800px;'})
    body = forms.CharField(required=True, label='Text', widget=body_w)

    tags_w = forms.TextInput(attrs={'list': 'tags'})
    tags = forms.CharField(required=False, label='Tags', max_length=100, widget=tags_w)
