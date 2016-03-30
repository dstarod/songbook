from django.shortcuts import render, redirect
from .models import Song, Tag

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views import generic


class SongsList(generic.ListView):
    # template_name = 'chords/index.html'
    context_object_name = 'songs'

    def get_queryset(self):
        # return Song.objects.all()
        return Song.objects.filter(user=self.request.user)


class SongDetail(generic.DetailView):
    model = Song
    # template_name = 'chords/song.html'


class TagList(generic.ListView):
    # template_name = 'chords/index.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)


class TagDetail(generic.DetailView):
    model = Tag
    # template_name = 'chords/song.html'


def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
        return redirect('songs:index')

    return render(request, template_name='chords/login.html')


def logout_view(request):
    logout(request)
    return redirect('songs:index')
