"""MinimalBookmark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^', include('bookmark.urls', namespace="bookmark")),
    url(r'^admin/', admin.site.urls),
]

# if not settings.DEBUG:
#     urlpatterns += patterns('',(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# ... the rest of your URLconf here ...

#urlpatterns += staticfiles_urlpatterns()




if not settings.DEBUG:
    #urlpatterns += patterns('django.contrib.staticfiles.views',url(r'^static/(?P<path>.*)$', 'serve'),)
    urlpatterns += staticfiles_urlpatterns()