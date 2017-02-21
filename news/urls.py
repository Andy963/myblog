#coding:utf-8
#! /usr/bin/env python

from django.conf.urls import url, include
from news.views import *

app_name = 'news'

#　main site
urlpatterns = [
               url(r'^$',IndexView.as_view(), name='index'),
]

# add ueditor to myblog
urlpatterns += [
	url(r'^ueditor/', include('DjangoUeditor.urls' )),
]

# login
urlpatterns += [

	url(r'^login$', login, name='login'),
	url(r'^verifyUser$', verifyUser, name='verifyUser'),
]

# skim
urlpatterns += [
	url(r'^(?P<article_id>\d+)/$', DetailView.as_view(), name='detail'),
	url(r'^(?P<article_id>\d+)/comment$', CommentView.as_view(), name='comment'),
]

urlpatterns += [
	url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',ArchiveView.as_view(),name="archive_month"),
]

from django.conf import settings

if settings.DEBUG:
	from django.conf.urls.static import static

	urlpatterns += static(
		settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)