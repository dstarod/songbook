from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views import generic

from .models import Song, Tag
from .forms import LoginForm, SongForm


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


def song_edit(request, pk):
    if int(pk) > 0:
        song = Song.objects.get(pk=pk)
    else:
        song = Song()

    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song.title = form.cleaned_data['title']
            song.body = form.cleaned_data['body']
            song.user = request.user
            song.save()

            tags = []

            form_tags = set([t.strip() for t in form.cleaned_data['tags'].upper().split(',')])
            existed_tags = Tag.objects.filter(title__in=form_tags, user=request.user).all()
            for tag in existed_tags:
                form_tags.discard(tag.title)
                tags.append(tag)

            for t in form_tags:
                if not len(t):
                    continue
                tag = Tag.objects.create(title=t, user=request.user)
                tags.append(tag)

            song.tags = tags
            song.save()

            return redirect('songs:edit', pk=song.id)

    f = SongForm(initial={
        'title': song.title,
        'body': song.body,
        'tags': ', '.join([t.title.upper() for t in song.tags.all()]) if song.title else ''
    })
    return render(request, 'chords/song_edit.html', context={'form': f, 'song_id': pk})


def login_view(request):
    login_form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = None
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
        if user is not None and user.is_active:
            login(request, user)
        return redirect('songs:index')

    return render(request, template_name='chords/login.html', context={'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('songs:index')
