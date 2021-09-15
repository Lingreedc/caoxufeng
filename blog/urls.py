from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^category/(?P<slug>[-_\w]+)/$', views.CategoryPostListView.as_view(), name='category_slug'),
    url(r'^tutorials/$', views.TutorialListView.as_view(), name='tutorials'),
    url(r'^categories/$', views.CategoryListView.as_view(), name='categories'),
    url(r'^archives/$', views.PostArchivesView.as_view(), name='archives'),
]
