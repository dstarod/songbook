from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, required=False)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput, required=False)


class SongForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label='Title')
    body = forms.CharField(required=True, label='Text', widget=forms.Textarea)
    tags = forms.CharField(required=False, label='Tags', max_length=100)
