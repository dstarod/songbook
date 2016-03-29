from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Song(models.Model):
    title = models.TextField(null=False)
    body = models.TextField(null=False, default='')
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now=True)

    user = models.ForeignKey(AUTH_USER_MODEL)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(AUTH_USER_MODEL)
    songs = models.ManyToManyField(Song, blank=True)

    def __str__(self):
        return self.title

# python3 manage.py createsuperuser
# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py sqlmigrate chords 0001
# python3 manage.py check
