from django.core.urlresolvers import reverse
from django.utils import timezone
from django.test import TestCase


from .models import Song


class SongTests(TestCase):

    def test_get_song_not_exists(self):
        new_song = Song(title='Hello')
        self.assertEquals(new_song.title, 'Hello')

    def test_view_list(self):
        Song.objects.create(title='Hello', body='Friend', user_id=1)
        response = self.client.get(reverse('songs:index'))
        self.assertQuerysetEqual(response.context['songs'], ['<Song: Hello>'])

    def test_view_detail(self):
        song = Song.objects.create(title='Hello', body='Friend', user_id=1)
        response = self.client.get(reverse('songs:song', args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['song'], song)
        self.assertContains(response, '<h3>Hello</h3>', status_code=200)
