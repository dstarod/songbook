from PIL import Image
from hashlib import md5
from django.db import models
from django.conf import settings
from django_resized import ResizedImageField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
import os
# from django.core.validators import

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


def validate_year(y):
    # https://docs.djangoproject.com/en/1.9/ref/validators/
    if y > datetime.utcnow().year:
        raise ValidationError(
            _('%(value)s year is in the future'),
            params={'value': y},
        )


def validate_pdf(y):
    if y.name.split('.')[-1] != 'pdf':
        raise ValidationError(
            _('%(value)s file is not PDF'),
            params={'value': y},
        )


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    ext = filename.split('.')[-1]
    fname = '{}.{}'.format(instance.pk, ext)
    path = '{0}/{1}'.format(instance.user.username.lower(), fname)
    os_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.isfile(os_path):
        os.remove(os_path)
    return '{0}/{1}'.format(instance.user.username.lower(), fname)


class Song(models.Model):
    title = models.CharField(null=False, max_length=100, verbose_name=_('Title'))
    body = models.TextField(null=False, blank=True, default='', verbose_name=_('Content'))
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name=_('Updated at'))
    user = models.ForeignKey(AUTH_USER_MODEL, editable=False, related_name='songs', verbose_name=_('User'))
    tags = models.ManyToManyField('Tag', blank=True, related_name="songs", verbose_name=_('Tags'))
    playlists = models.ManyToManyField('Playlist', related_name='songs', blank=True, verbose_name=_('Playlists'))
    public = models.BooleanField(default=False, null=False, verbose_name=_('Public'))
    approved = models.BooleanField(default=False, null=False, verbose_name=_('Approved'))

    pdf = models.FileField(upload_to=user_directory_path, verbose_name='PDF', validators=[validate_pdf], null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def body_nbsp(self):
        return self.body.replace(' ', '&nbsp;')


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    user = models.ForeignKey(AUTH_USER_MODEL, editable=False)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, related_name='profile')
    image = ResizedImageField(upload_to='avatars')


class Playlist(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False, verbose_name=_('Title'))
    user = models.ForeignKey(AUTH_USER_MODEL, related_name='playlists')

    def __str__(self):
        return self.title


class SongProfile(models.Model):
    song = models.OneToOneField(Song, related_name='profile')
    author = models.CharField(max_length=256, null=False, verbose_name=_('Author'))
    composer = models.CharField(max_length=256, null=False, verbose_name=_('Composer'))
    translator = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('Translator'))
    year = models.PositiveSmallIntegerField(validators=[validate_year], blank=True, null=True, verbose_name=_('Year'))

    def __str__(self):
        return self.author

# python3 manage.py createsuperuser
# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py sqlmigrate chords 0001
# python3 manage.py check

# TODO: Users group. Email to users.
# TODO: Playlist. Shared to user/group for read only / edit.
