from django.contrib import admin

from posts.models import Category, Post, Comment, PostView


class postAdmin(admin.ModelAdmin):
    list_display=('title','author','pub_date','timestamp','created_date', 'was_published_recently')
    list_filter = ('author', 'publish', )
    fieldsets = [
        ('Overview',               {'fields': ['title','overview','thumbnail']}),
        (None,               {'fields': ['content','publish', 'read_time']}),
        ('Tagging', {'fields': ['author', 'categories', 'previous_post', 'next_post'],
         'classes': ['collapse']}),
    ]

admin.site.register(Category)
admin.site.register(Post, postAdmin)
admin.site.register(Comment)
admin.site.register(PostView)
