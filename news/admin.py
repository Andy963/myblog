from django.contrib import admin
from .models import Article, Author, Tag, Category, Comment
# Register your models here.

# you also can use the decorator :@admin.register(Article)



class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'clickCount', 'isRecommend')
	search_fields = ('title', 'pub_date')
	# if you set actions_on_bottom = True, there will have action at bottom ,so you have two
	#actions_on_bottom = True;

	actions = ['Recommend']
	def Recommend(self, request, queryset):
		rows_updated = queryset.update(isRecommend=1)
		if rows_updated == 1:
			message_bit = "1 article was"
		else:
			message_bit = "%s articles were" % rows_updated
		self.message_user(request, "%s successfully Recommend." % message_bit)

	Recommend.short_description = "Recommend article（推荐文章）"

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
	actions = ['select_gender']

	def select_gender(self, request, queryset):
		rows_updated = queryset.update(gender=2)
		if rows_updated == 1:
			message_bit = "1 author was"
		else:
			message_bit = "%s authors were" % rows_updated
		self.message_user(request, "%s successfully changed." % message_bit)

	select_gender.short_description = "selected Author's gender"

	list_display = ('name','gender','birthday','registerTime','latestLogTime','email','total_blog')
	search_fields = ('name','email','birthday','total_blog')

	fieldsets = (
		('基本信息：', {
			'fields': (('name','gender'),'birthday','email' )
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


