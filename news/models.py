import datetime
from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


# create a common base class
# 作者
@python_2_unicode_compatible
class Author(models.Model):
	name = models.CharField(verbose_name = "姓名", max_length=20)
	sex = models.IntegerField(verbose_name= '性别', blank=True, null=True)
	birthday = models.DateTimeField(verbose_name= '生日', blank=True, null=True)
	registerTime = models.DateTimeField(verbose_name= '注册日期', blank=True, null=True)
	latestLogTime = models.DateTimeField(verbose_name='最近登陆日期', blank=True, null=True)
	email = models.EmailField(verbose_name = "邮件",blank=True, null=True)
	total_blog = models.IntegerField(verbose_name = "文章总数", default=0)

	# if you want to use ImageField you should install pillow
	#avatar = models.ImageField(upload_to = 'photos')

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


# 文章
@python_2_unicode_compatible
class Article(models.Model):
	title = models.CharField(verbose_name = '标题', max_length=200)
	content = models.TextField(verbose_name = '内容', max_length=10000)
	pub_date = models.DateTimeField(verbose_name = '发布日期', default=timezone.now)
	update_date = models.DateTimeField(verbose_name= '最近修改日期',default=timezone.now)
	clickCount = models.IntegerField(verbose_name = '浏览次数', default=0)
	isRecommend = models.BooleanField(verbose_name='推荐',default=False)

	#comment = models.TextField(verbose_name = '评论',max_length=200,blank=True, null=True)
	# models.CASCADE django will delete related database
	author = models.ForeignKey(Author, verbose_name= '作者',on_delete=models.CASCADE)
	category = models.ForeignKey(Category, verbose_name='分类', blank=True, null=True)
	tag = models.ManyToManyField(Tag, verbose_name='标签',blank=True)

	class Meta:
		# ordering with pub_date decreasing then browse increasing
		ordering = ['-pub_date', 'clickCount']
		# specify the verbose name
		verbose_name = '文章'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.title


# 评论
@python_2_unicode_compatible
class Comment(models.Model):
	content = models.TextField(verbose_name= '评论内容',max_length= 200)
	pub_date = models.DateTimeField(verbose_name='发布日期', default=timezone.now)
	author = models.ForeignKey(Author, verbose_name='评论作者')
	article = models.ForeignKey(Article, verbose_name='文章')
	pid = models.ForeignKey('self', verbose_name='父级评论',blank=True, null=True)

	class Meta:
		# ordering with pub_date decreasing then browse increasing
		ordering = ['-pub_date', ]
		verbose_name = '评论'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.pid