# coding: utf-8
import datetime
from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from DjangoUeditor.models import UEditorField
import collections

from django.contrib.auth.models import User
# Create your models here.


# create a common base class
# 作者
@python_2_unicode_compatible
class Author(models.Model):

	GENDER = (
			(0,'male'),
			(1, 'female'),
			(2, 'unknown'),)

	name = models.CharField(verbose_name = "姓名", max_length=20,unique=True)
	gender = models.IntegerField(choices= GENDER, verbose_name= '性别', default=2)
	birthday = models.DateTimeField(verbose_name= '生日', blank=True, null=True)
	register_time = models.DateTimeField(verbose_name= '注册日期', blank=True, null=True)
	latest_log_time = models.DateTimeField(verbose_name='最近登陆日期', blank=True, null=True)
	email = models.EmailField(verbose_name = "邮件",blank=True, null=True)
	total_blog = models.IntegerField(verbose_name = "文章总数", default=0)
	account = models.OneToOneField(User,verbose_name = "账号",unique=True, on_delete = models.CASCADE)


	class Meta:
		verbose_name = '作者'
		verbose_name_plural = verbose_name
		ordering = ['name', 'total_blog']

	def __str__(self):
		return self.name


# 分类
@python_2_unicode_compatible
class Category(models.Model):
	name = models.CharField(verbose_name='分类名称', max_length=30)
	index = models.IntegerField(verbose_name='分类排序', default=999)

	class Meta:
		verbose_name = '分类'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


# 标签
@python_2_unicode_compatible
class Tag(models.Model):
	name = models.CharField(verbose_name='标签', max_length=30)

	class Meta:
		verbose_name = '标签'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name

class ArticleManage(models.Manager):
	def archive(self):
		date_list = Article.objects.datetimes('pub_date', 'month', order='DESC')
		year_month = collections.OrderedDict()
		for date in date_list:
			if not year_month.get(date.year):
				year_month[date.year] = []
				year_month[date.year].append(date.month)
			elif year_month.get(date.year):
				year_month[date.year].append(date.month)
		return(year_month)

# 文章
@python_2_unicode_compatible
class Article(models.Model):
	objects = ArticleManage()

	RECOMMEND = (
		(0, 'not_recommend'),
		(1, 'recommend'),
	)

	STATUS = (
		('d', 'Draft'),
		('p', 'Published'),
		('w', 'Withdrawn'),
	)

	title = models.CharField(verbose_name = '标题', max_length=200)
	#content = models.TextField(verbose_name = '内容', max_length=10000)
	content = UEditorField('内容', height=300, width=1000,default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')
	pub_date = models.DateTimeField(verbose_name = '发布日期', default=timezone.now)
	update_date = models.DateTimeField(verbose_name= '最近修改日期',default=timezone.now)
	click_count = models.IntegerField(verbose_name = '浏览次数', default=0)
	recommend = models.IntegerField(choices=RECOMMEND, verbose_name='推荐',default=False)
	status = models.CharField(choices=STATUS, verbose_name='状态',default='d',max_length=10)
	author = models.ForeignKey(Author, verbose_name= '作者',on_delete=models.CASCADE)
	category = models.ForeignKey(Category, verbose_name='分类', blank=True, null=True)
	tag = models.ManyToManyField(Tag, verbose_name='标签',blank=True)

	def get_absolute_url(self):
		# 这里 reverse 解析 blog:detail 视图函数对应的 url
		return reverse('news:detail', kwargs={'article_id': self.pk})

	class Meta:
		# ordering with pub_date decreasing then browse increasing
		ordering = ['-pub_date', 'click_count']
		# specify the verbose name
		verbose_name = '文章'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.title





# 评论
@python_2_unicode_compatible
class Comment(models.Model):
	content = models.TextField(verbose_name= '评论内容',max_length= 200)
	pub_date = models.DateTimeField(verbose_name='发布日期', auto_now_add=True)
	author = models.ForeignKey(Author, verbose_name='评论作者')
	article = models.ForeignKey(Article, verbose_name='评论所属文章', on_delete=models.CASCADE)
	count = models.IntegerField(verbose_name='评论次数',default=0)
	pid = models.ForeignKey('self', verbose_name='父级评论',blank=True, null=True)

	class Meta:
		# ordering with pub_date decreasing then browse increasing
		ordering = ['-pub_date', ]
		verbose_name = '评论'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.pid