from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


from . import views

urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.showHome, name='index'),
    url(r'^bookmark/(?P<url_id>[0-9]+)/$', views.showDetails, name='show'),
    url(r'^tags/(?P<tag_id>[0-9]+)/$', views.showTag, name='showTag'),
    url(r'^tags/$', views.showTags, name='showTags'),
    url(r'^tags/new/$', views.addTag, name='addTag'),
    url(r'^tags/new/insertTagAndShow/$', views.insertTagAndShow, name='InsertTagAndShow'),
    url(r'^tags/(?P<tag_id>[0-9]+)/edit$', views.editTag, name='editTag'),
    url(r'^tags/updateTagAndShow/(?P<tag_id>[0-9]+)/$', views.updateTagAndShow, name='updateTag'),
    url(r'^bookmark/(?P<url_id>[0-9]+)/edit$', views.editURL, name='editURL'),
    url(r'^bookmark/updateBookmarkAndShow/(?P<url_id>[0-9]+)/$', views.updateBookmarkAndShow, name='updateBookmarkAndShow'),
    url(r'^addBookmark$', views.addBookmark, name='addBookmark'),
    url(r'^searchBookmark$', views.searchBookmark, name='searchBookmark'),
    url(r'^tags/destroyTag$', views.destroyTag, name='destroyTag'),
    url(r'^destroyBookmark$', views.destroyBookmark, name='destroyBookmark'),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns



if not settings.DEBUG:
    #urlpatterns += patterns('django.contrib.staticfiles.views',url(r'^static/(?P<path>.*)$', 'serve'),)
    urlpatterns += staticfiles_urlpatterns()