from django.conf.urls import url

from . import views

app_name = 'blog_andy'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name = 'archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoriesView.as_view(), name = 'categories'),
]