from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', login_required(views.SongsList.as_view()), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.SongDetail.as_view()), name='song'),

    url(r'^tag/(?P<pk>[0-9]+)/$', login_required(views.TagDetail.as_view()), name='tag'),
    url(r'^tags/$', login_required(views.TagList.as_view()), name='tags'),

    url(r'login', views.login_view, name='login'),
    url(r'logout/$', views.logout_view, name='logout'),

    url(r'^edit/(?P<pk>[0-9]+)', views.song_edit, name='edit'),
]

# from django.contrib.auth.decorators import permission_required
# url(r'^vote/', permission_required('polls.can_vote')(VoteView.as_view())),
