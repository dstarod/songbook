from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^accounts/profile/$', views.profile),

    url(r'^$', views.SongsList.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.SongDetail.as_view(), name='song'),
    url(r'^edit/(?P<pk>[0-9]+)$', login_required(views.SongEdit.as_view()), name='edit'),
    url(r'^create/$', login_required(views.SongCreate.as_view()), name='create'),
    url(r'^delete/(?P<pk>[0-9]+)$', login_required(views.SongDelete.as_view()), name='delete'),

    url(r'^tag/(?P<pk>[0-9]+)/$', login_required(views.TagDetail.as_view()), name='tag'),
    url(r'^tags/$', login_required(views.TagList.as_view()), name='tags'),
    url(r'^tags/create/$', login_required(views.TagCreate.as_view()), name='tag_create'),
    url(r'^tags/edit/(?P<pk>[0-9]+)$', login_required(views.TagEdit.as_view()), name='tag_edit'),
    url(r'^tags/delete/(?P<pk>[0-9]+)$', login_required(views.TagDelete.as_view()), name='tag_delete'),
]

# from django.contrib.auth.decorators import permission_required
# url(r'^vote/', permission_required('polls.can_vote')(VoteView.as_view())),
