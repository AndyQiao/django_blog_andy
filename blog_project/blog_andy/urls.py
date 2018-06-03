from django.conf.urls import url

from . import views

app_name = 'blog_andy'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', views.archives, name = 'archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.categories, name = 'categories'),
]