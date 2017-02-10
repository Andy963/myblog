#coding:utf-8

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


# use myself logger
logger = logging.getLogger("blogLogger")

class IndexView(generic.ListView):
	template_name = 'news/index.html'
	context_object_name = 'title_list'

	def get_queryset(self):
		# return the last five published blog
		return Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]




class DetailView(generic.DetailView):
	model = Article
	template_name = 'news/detail.html'
	#context_object_name = 'blog'

	def get_queryset(self):

		return Article.objects.filter(pub_date__lte=timezone.now())

	def get(self, request, *args, **kwargs):
		# 根据文章的id 对每一次点击累加
		article = Article.objects.get(id=kwargs['article_id'])
		clickCount = article.clickCount
		clickCount += 1
		article.clickCount = clickCount
		article.save()

		# Show comment_list at detail html
		comment_list = article.comment_set.all()

		return render(request, 'news/detail.html', {'blog': article, 'comment_list': comment_list})

	# 新增 form 到 context
	def get_context_data(self, **kwargs):
		kwargs['comment_list'] = self.object.comment_set.all()
		kwargs['form'] = CommentForm()
		return super(DetailView, self).get_context_data(**kwargs)


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

# log on
def login(request):
	return render(request, 'news/login.html')

# virify if user is valid
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
	template_name = 'news/detail.html'

	def form_valid(self, form):
		targetArticle = get_object_or_404(Article, pk=self.kwargs['article_id'])
		comment =  form.save(commit=False)
		comment.article = targetArticle
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

