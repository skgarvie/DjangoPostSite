from django.contrib import admin
from posts.models import Post, Comment
# Register your models here.

class CommentInline(admin.TabularInline):
	model=Comment
	extra = 3

class PostAdmin(admin.ModelAdmin):
	list_display = ('content','pub_date','was_published_recently')
	list_filter=['pub_date']
	search_fields = ['content']

	fieldsets = [
		(None,{'fields':['content']}),
		('Date Information',{'fields':['pub_date'],'classes':['collapse']}),
	]
	
	inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
