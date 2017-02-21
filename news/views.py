#coding:utf-8
#!/usr/bin/env python


from django.shortcuts import render, get_object_or_404,render_to_response
from django.views import generic
from django.views.generic.edit import FormView
from .models import Article, Author, Comment
from django.utils import timezone
import datetime
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
import logging
from .forms import CommentForm
from django.views.generic.dates import MonthArchiveView
from django.core.urlresolvers import reverse
# use myself logger
logger = logging.getLogger("blogLogger")

"""
def Index(request):
	title_list = Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
	article_list = Article.objects.datetimes('pub_date', 'month', order='DESC')
	return render(request, 'news/index.html', {'title_list':title_list, 'article_list': article_list})


"""
class IndexView(generic.ListView):
	template_name = 'news/index.html'
	context_object_name = 'title_list'

	def get_queryset(self):
		# return the last five published blog
		return Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

	def get_context_data(self, **kwargs):
		kwargs['month_archive'] = Article.objects.archive()
		return super(IndexView, self).get_context_data(**kwargs)


class ArchiveView(generic.ListView):
	template_name = "news/article_archive_month.html"
	context_object_name = "title_list"
	def get_queryset(self):
		year = int(self.kwargs['year'])
		month = int(self.kwargs['month'])
		article_list = Article.objects.filter(pub_date__year=year, pub_date__month=month)
		return article_list


class DetailView(generic.DetailView):
	model = Article
	template_name = 'news/detail.html'
	#context_object_name = 'blog'

	def get_queryset(self):
		return Article.objects.filter(pub_date__lte=timezone.now())

	def get(self, request, *args, **kwargs):
		# 根据文章的id 对每一次点击累加
		article = Article.objects.get(id=kwargs['article_id'])
		click_count = article.click_count
		click_count += 1
		article.click_count = click_count
		article.save()

		# Show comment_list at detail html
		comment_list = article.comment_set.all()
		context = {'article': article, 'comment_list': comment_list}

		return render(request, 'news/detail.html', context)

	# 新增 form 到 context
	def get_context_data(self, **kwargs):

		kwargs['form'] = CommentForm()
		return super(DetailView, self).get_context_data(**kwargs)

# log on
def login(request):
	return render(request, 'news/login.html')

# verify if user is valid
def verifyUser(request):
	if request.method == 'POST':
		tips = 'Invalid user name or password, please try again!'
		user_name = request.POST['username']
		password = request.POST['pwd']
		try:
			user = auth.authenticate(username=user_name, password=password)
			if user is not None and user.is_active:
				auth.login(request, user)
				return HttpResponseRedirect("../news")
			else:
				return render_to_response('news/login.html', {'tips': tips}, RequestContext(request,\
				{'username': user_name,'password': password}))
		except Exception as e:
			logger.error(e)


class CommentView(FormView):
	form_class = CommentForm
	template_name = 'news/comment.html'

	def form_valid(self, form):
		targetArticle = get_object_or_404(Article, pk=self.kwargs['article_id'])
		comment =  form.save(commit=False)
		comment.article = targetArticle
		# get the count of comment
		comment_count = targetArticle.comment_set.count()
		comment_count += 1
		comment.save()

		self.success_url = targetArticle.get_absolute_url()
		return HttpResponseRedirect(self.success_url)

	def form_invalid(self, form):
		"""提交的数据验证不合法后的逻辑"""
		targetArticle = get_object_or_404(Article, pk=self.kwargs['article_id'])
		# 不保存评论，回到原来提交评论的文章详情页面
		return render(self.request, 'news/detail.html', {
			'form': form,
			'article': targetArticle,
			'comment_list': targetArticle.comment_set.all(),
		})



