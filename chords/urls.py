from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login', views.my_login),
    url(r'enter/$', views.my_view, name='login'),
    url(r'logout/$', views.logout_view, name='logout'),
]
