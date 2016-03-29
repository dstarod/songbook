from django.shortcuts import render, redirect
from .models import Song

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


@login_required
def index(request):
    if request.user.is_authenticated():
        print(request.user)
    songs = Song.objects.filter(user=request.user)
    context = dict(songs=songs)
    return render(request, template_name='chords/index.html', context=context)


def my_login(request):
    return render(request, template_name='chords/login.html')


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
    return redirect('songs:index')


def logout_view(request):
    logout(request)
    return redirect('songs:index')
