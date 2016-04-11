from PIL import Image
from django.db import models
from django.conf import settings
from django_resized import ResizedImageField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
# from django.core.validators import

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


def validate_year(y):
    # https://docs.djangoproject.com/en/1.9/ref/validators/
    if y > datetime.utcnow().year:
        raise ValidationError(
            _('%(value)s year is in the future'),
            params={'value': y},
        )


class Song(models.Model):
    title = models.CharField("song's title", null=False, max_length=100)
    body = models.TextField("song's text", null=False, default='')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    user = models.ForeignKey(AUTH_USER_MODEL, editable=False)
    tags = models.ManyToManyField('Tag', blank=True, related_name="songs")

    public = models.BooleanField('public', default=False, null=False)
    approved = models.BooleanField('approved', default=False, null=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def body_nbsp(self):
        return self.body.replace(' ', '&nbsp;')


class Tag(models.Model):
    title = models.CharField("Song's tag", max_length=100)
    user = models.ForeignKey(AUTH_USER_MODEL, editable=False)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, related_name='profile')
    # image = models.ImageField(upload_to='avatars')
    image = ResizedImageField(upload_to='avatars')


class SongProfile(models.Model):
    song = models.OneToOneField(Song, related_name='profile')
    author = models.CharField(max_length=256, null=False)
    composer = models.CharField(max_length=256, null=False)
    translator = models.CharField(max_length=256, blank=True, null=True)
    year = models.PositiveSmallIntegerField(validators=[validate_year], blank=True, null=True)

    def __str__(self):
        return self.author

# python3 manage.py createsuperuser
# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py sqlmigrate chords 0001
# python3 manage.py check

# TODO: Song info: Author, composer, translator, year. Public approved if info filled.
# TODO: Users group. Email to users.
# TODO: Playlist. Shared to user/group for read only / edit.
