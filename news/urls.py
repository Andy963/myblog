#coding:utf-8
#! /usr/bin/env python

from django.conf.urls import url, include
from news.views import *

app_name = 'news'

#　main site
urlpatterns = [
               url(r'^$',IndexView.as_view(), name='index'),
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