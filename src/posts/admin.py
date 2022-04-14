from django.contrib import admin

from posts.models import Author, Category, Post

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
