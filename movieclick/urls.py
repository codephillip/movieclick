from django.conf.urls import url
from django.contrib import admin

from movie import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^browse/(?P<pk>[-\w]+)/$', views.browse, name='browse'),
    url(r'^search/$', views.search, name='search'),
    url(r'^download/(?P<pk>[-\w]+)/$', views.download, name='download'),
    url(r'^watch/(?P<pk>[-\w]+)/$', views.watch, name='watch'),
]
