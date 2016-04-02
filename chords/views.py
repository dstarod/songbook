from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from .models import Song, Tag
from .forms import LoginForm, SongModelForm
from django.db.models import Q


class SongsList(generic.ListView):
    context_object_name = 'songs'

    def get_queryset(self):
        # Only users songs or public
        return Song.objects.filter(Q(user_id=self.request.user.id) | Q(public=True))


class SongDetail(generic.DetailView):
    model = Song

    def get_queryset(self):
        # Only users songs or public
        return Song.objects.filter(Q(user_id=self.request.user.id) | Q(public=True))


class SongEdit(generic.UpdateView):
    model = Song
    form_class = SongModelForm
    success_url = reverse_lazy('songs:index')

    def get_initial(self, *args, **kwargs):
        # Get only user tags
        super(SongEdit, self).get_initial()
        self.initial = {'user': self.request.user}
        return self.initial

    def get_queryset(self):
        # Only users songs or public
        return Song.objects.filter(user_id=self.request.user.id)


class SongCreate(generic.CreateView):
    model = Song
    form_class = SongModelForm
    success_url = reverse_lazy('songs:index')

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
    success_url = reverse_lazy('songs:index')

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
    success_url = reverse_lazy('songs:tags')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TagCreate, self).form_valid(form)


class TagDelete(generic.DeleteView):
    model = Tag
    template_name = 'chords/tag_delete.html'
    success_url = reverse_lazy('songs:tags')

    def get_queryset(self):
        # Only users songs or public
        return Tag.objects.filter(user_id=self.request.user.id)


class TagEdit(generic.UpdateView):
    model = Tag
    fields = ['title']
    success_url = reverse_lazy('songs:tags')


def profile(request):
    return render(request, template_name='chords/song.html', context={})
