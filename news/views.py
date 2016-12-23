#coding:utf-8

from django.shortcuts import render, get_object_or_404,render_to_response
from django.http import HttpResponse
from django.views import generic
from .models import Article, Author
from django.utils import timezone
import datetime
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
import logging

# use myself logger
logger = logging.getLogger("blogLogger")

class IndexView(generic.ListView):
	template_name = 'news/index.html'
	context_object_name = 'title_list'

	def get_queryset(self):
		# return the last ten published blog
		return Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]




class DetailView(generic.DetailView):
	model = Article
	template_name = 'news/detail.html'
	context_object_name = 'blog'

	def get_queryset(self):

		return Article.objects.filter(pub_date__lte=timezone.now())

	def get(self, request, *args, **kwargs):
		# 根据文章的id 对每一次点击累加
		blog = Article.objects.get(id=kwargs['pk'])
		clickCount = blog.clickCount
		clickCount += 1
		blog.clickCount = clickCount
		blog.save()
		return render(request, 'news/detail.html', {'blog': blog})


"""
def get_query(request, pk=''):
# 根据文章的id 对每一次点击累加
	blog = Article.objects.get(id=pk)
	browses = blog.browse
	browses += 1
	blog.browse = browses
	blog.save()
	#obj = Article.objects.filter(pub_date__lte=timezone.now())
	return render(request, 'news/detail.html',{'blog':blog})
"""

def login(request):
	# some test of logger
	try:
		# example
		file = open('xxx.txt', 'r')
	except Exception as e:
		logger.error(e)
	return render(request, 'news/login.html')

def verifyUser(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['pwd']
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			return HttpResponseRedirect("../news")
		else:
			return render_to_response('news/login.html',RequestContext(request, {'username': username, 'password_is_wrong': True}))
