from django.contrib import admin
from .models import Article, Author, Tag, Category, Comment
# Register your models here.

# you also can use the decorator :@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'clickCount')
	search_fields = ('title', 'pub_date')
	actions_on_bottom = True;
	empty_value_display = '-empty-'
	fieldsets = (
		('基本内容：',{
			'fields':('title', 'content', ( "author",'category','isRecommend'))
		}),

		('高级选项：', {
			'classes': ('collapse',),
			'fields': ("tag",),
		}),
	)

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name','sex','birthday','registerTime','latestLogTime','email','total_blog')
	search_fields = ('name','email','birthday','total_blog')

	fieldsets = (
		('基本信息：', {
			'fields': (('name','sex'),'birthday','email' )
		}),

		('高级选项：', {
			'classes': ('collapse',),
			'fields': ('registerTime',),
		}),
	)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('author', 'article','pub_date','content')
	search_fields = ('author','article', 'content')

	fieldsets = (
		('基本信息：', {
			'fields': ('article','author','content' )
		}),

		('高级选项：', {
			'classes': ('collapse',),
			'fields': ('pub_date',),
		}),
	)

admin.site.register(Article,ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)


