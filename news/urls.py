#coding:utf-8
#! /usr/bin/env python

from django.conf.urls import url, include
from . import views

app_name = 'news'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^login$', views.login, name='login'),
	url(r'^verifyUser$', views.verifyUser, name='verifyUser'),
	url(r'^(?P<article_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<article_id>\d+)/comment$', views.CommentView.as_view(), name='comment'),
	#url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	#url(r'^(?P<pk>[0-9]+)/$', views.get_query, name='detail'),

]
