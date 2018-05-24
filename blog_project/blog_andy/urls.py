from django.conf.urls import url

from . import views

app_name = 'blog_andy'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]