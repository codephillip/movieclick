from django.conf.urls import url
from django.contrib import admin

from movie import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^browse/(?P<year>[-\w]+)/(?P<pk>[-\w]+)/$', views.browse, name='browse'),
    url(r'^search/$', views.search, name='search'),
    url(r'^updatedb/$', views.update_db, name='update_db'),
    url(r'^remove_adblocker/$', views.remove_adblocker, name='remove_adblocker'),
    url(r'^download/(?P<pk>[-\w]+)/$', views.download, name='download'),
    url(r'^watch/(?P<pk>[-\w]+)/$', views.watch, name='watch'),
    url(r'^movie_not_found/(?P<pk>[-\w]+)/$', views.movie_not_found, name='movie_not_found'),
]
