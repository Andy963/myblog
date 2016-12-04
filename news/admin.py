from django.contrib import admin
from .models import Article, Author, Tag, Category, Comment
# Register your models here.

# you also can use the decorator :@admin.register(Text)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'clickCount')
	search_fields = ('title', 'pub_date')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)


