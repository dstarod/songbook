from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from .models import Song, Tag, SongProfile, Playlist
from .forms import LoginForm, SongModelForm
from django.db.models import Q


class PlaylistList(generic.ListView):
    context_object_name = 'playlists'
    paginate_by = 10

    def get_queryset(self):
        # Only users songs or public
        # return Song.objects.filter(Q(user_id=self.request.user.id) | Q(public=True))
        return Playlist.objects.filter(user_id=self.request.user.id)


class PlaylistDetails(generic.DetailView):
    context_object_name = 'playlist'
    model = Playlist

    def get_queryset(self):
        # Only users songs or public
        return Playlist.objects.filter(songs__user_id=self.request.user.id)


# TODO Add and Edit playlist


class SongsList(generic.ListView):
    context_object_name = 'songs'
    # https://docs.djangoproject.com/en/1.9/topics/pagination/
    paginate_by = 10

    def get_queryset(self):
        # Only users songs or public
        # return Song.objects.filter(Q(user_id=self.request.user.id) | Q(public=True))
        return Song.objects.filter(user_id=self.request.user.id)


class SongsListPublic(generic.ListView):
    context_object_name = 'songs'

    def get_queryset(self):
        # Only users songs or public
        return Song.objects.filter(Q(public=True) & Q(approved=True))


class SongDetail(generic.DetailView):
    model = Song

    def get_queryset(self):
        # Only users songs or public
        return Song.objects.filter(Q(user_id=self.request.user.id) | Q(public=True))


class SongProfileCreate(generic.CreateView):
    model = SongProfile
    success_url = reverse_lazy('songs:song_list')
    fields = ('author', 'composer', 'year', 'translator')

    def form_valid(self, form):
        form.instance.song_id = self.kwargs['pk']
        return super(SongProfileCreate, self).form_valid(form)

    def get_queryset(self):
        # Only users songs
        return SongProfile.objects.filter(song__user_id=self.request.user.id)


class SongProfileEdit(generic.UpdateView):
    model = SongProfile
    success_url = reverse_lazy('songs:song_list')
    fields = ('author', 'composer', 'year', 'translator')

    def get_queryset(self):
        # Only users songs
        return SongProfile.objects.filter(song__user_id=self.request.user.id)


class SongEdit(generic.UpdateView):
    model = Song
    form_class = SongModelForm
    # success_url = reverse_lazy('songs:song_list')

    def get_success_url(self):
        return reverse_lazy('songs:song', kwargs=self.kwargs)

    def get_initial(self, *args, **kwargs):
        # Get only user tags
        super(SongEdit, self).get_initial()
        self.initial = {'user': self.request.user}
        return self.initial

    def get_queryset(self):
        # Only users songs
        return Song.objects.filter(user_id=self.request.user.id)


class SongCreate(generic.CreateView):
    model = Song
    form_class = SongModelForm
    success_url = reverse_lazy('songs:song_list')

    def get_initial(self, *args, **kwargs):
        # Get only user tags
        super(SongCreate, self).get_initial()
        self.initial = {'user': self.request.user}
        return self.initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SongCreate, self).form_valid(form)


class SongDelete(generic.DeleteView):
    model = Song
    template_name = 'chords/song_delete.html'
    success_url = reverse_lazy('songs:song_list')

    def get_queryset(self):
        # Only users songs or public
        return Song.objects.filter(user_id=self.request.user.id)


class TagList(generic.ListView):
    # template_name = 'chords/index.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)


class TagDetail(generic.DetailView):
    model = Tag

    def get_queryset(self):
        # Only users songs or public
        return Tag.objects.filter(user_id=self.request.user.id)


class TagCreate(generic.CreateView):
    model = Tag
    fields = ['title']
    success_url = reverse_lazy('songs:tag_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TagCreate, self).form_valid(form)


class TagDelete(generic.DeleteView):
    model = Tag
    template_name = 'chords/tag_delete.html'
    success_url = reverse_lazy('songs:tag_list')

    def get_queryset(self):
        # Only users songs or public
        return Tag.objects.filter(user_id=self.request.user.id)


class TagEdit(generic.UpdateView):
    model = Tag
    fields = ['title']
    success_url = reverse_lazy('songs:tag_list')


def profile(request):

    return render(request, template_name='registration/profile.html', context={})
