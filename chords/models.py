from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Song(models.Model):
    title = models.CharField("song's title", null=False, max_length=100)
    body = models.TextField("song's text", null=False, default='')
    public = models.BooleanField('public', default=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    tags = models.ManyToManyField('Tag', blank=True, related_name="songs")
    user = models.ForeignKey(AUTH_USER_MODEL)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField("Song's tag", max_length=100)
    user = models.ForeignKey(AUTH_USER_MODEL)

    def __str__(self):
        return self.title

#
# class SongTag(models.Model):
#     song = models.ForeignKey(Song)
#     tag = models.ForeignKey(Tag)
#     user = models.ForeignKey(AUTH_USER_MODEL)


# python3 manage.py createsuperuser
# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py sqlmigrate chords 0001
# python3 manage.py check
