from django import forms
from .models import Song, Tag, SongProfile, Playlist


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, required=False)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput, required=False)


class SongModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # Get only user tags
        super(SongModelForm, self).__init__(*args, **kwargs)
        user = kwargs.get('initial', {}).get('user', None)
        self.fields['tags'].queryset = Tag.objects.filter(user=user)
        self.fields['playlists'].queryset = Playlist.objects.filter(user=user)

    class Meta:
        model = Song
        fields = ['title', 'tags', 'body', 'public', 'playlists']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Song title'}),
            'body': forms.Textarea(attrs={
                'class': 'song_body_edit materialize-textarea'
            })
        }
