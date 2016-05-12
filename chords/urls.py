from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^accounts/profile/$', views.profile),

    url(r'^$', views.SongsListPublic.as_view(), name='index'),

    url(r'^song/(?P<pk>[0-9]+)/$', views.SongDetail.as_view(), name='song'),
    url(r'^song/list/$', login_required(views.SongsList.as_view()), name='song_list'),
    url(r'^song/edit/(?P<pk>[0-9]+)/$', login_required(views.SongEdit.as_view()), name='song_edit'),
    url(r'^song/profile/create/(?P<pk>[0-9]+)/$', login_required(views.SongProfileCreate.as_view()), name='song_profile_create'),
    url(r'^song/profile/edit/(?P<pk>[0-9]+)/$', login_required(views.SongProfileEdit.as_view()), name='song_profile_edit'),
    url(r'^song/create/$', login_required(views.SongCreate.as_view()), name='song_create'),
    url(r'^song/delete/(?P<pk>[0-9]+)/$', login_required(views.SongDelete.as_view()), name='song_delete'),

    url(r'^song/copy/(?P<pk>[0-9]+)/$', login_required(views.copy_song), name='song_copy'),

    url(r'^tag/(?P<pk>[0-9]+)/$', login_required(views.TagDetail.as_view()), name='tag'),
    url(r'^tag/list/$', login_required(views.TagList.as_view()), name='tag_list'),
    url(r'^tag/create/$', login_required(views.TagCreate.as_view()), name='tag_create'),
    url(r'^tag/edit/(?P<pk>[0-9]+)/$', login_required(views.TagEdit.as_view()), name='tag_edit'),
    url(r'^tag/delete/(?P<pk>[0-9]+)/$', login_required(views.TagDelete.as_view()), name='tag_delete'),

    url(r'^playlist/list/$', login_required(views.PlaylistList.as_view()), name='playlist_list'),
    url(r'^playlist/(?P<pk>[0-9]+)/$', login_required(views.PlaylistDetails.as_view()), name='playlist'),
    url(r'^playlist/edit/(?P<pk>[0-9]+)/$', login_required(views.PlaylistEdit.as_view()), name='playlist_edit'),
    url(r'^playlist/delete/(?P<pk>[0-9]+)/$', login_required(views.PlaylistDelete.as_view()), name='playlist_delete'),
    url(r'^playlist/create/$', login_required(views.PlaylistCreate.as_view()), name='playlist_create'),
]

# from django.contrib.auth.decorators import permission_required
# url(r'^vote/', permission_required('polls.can_vote')(VoteView.as_view())),
