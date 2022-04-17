from django.contrib import admin

from posts.models import Author, Category, Post, Comment, PostView

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
