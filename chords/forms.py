from django import forms
from .models import Song, Tag, SongProfile, Playlist
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, required=False)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput, required=False)


class SongProfileModelForm(forms.ModelForm):
    class Meta:
        model = SongProfile
        fields = ['author', 'composer', 'translator', 'year']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'composer': forms.TextInput(attrs={'class': 'form-control'}),
            'translator': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SongModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # Get only user tags
        super(SongModelForm, self).__init__(*args, **kwargs)
        user = kwargs.get('initial', {}).get('user', None)
        self.fields['tags'].queryset = Tag.objects.filter(user=user)
        self.fields['playlists'].queryset = Playlist.objects.filter(user=user)

    class Meta:
        model = Song
        fields = ['title', 'body', 'tags', 'playlists', 'public']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Song title'
            }),
            'body': forms.Textarea(attrs={
                'class': 'song_body'
            }),
            'tags': forms.CheckboxSelectMultiple(),
            'playlists': forms.CheckboxSelectMultiple(),
        }
