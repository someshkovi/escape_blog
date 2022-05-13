from django.contrib import admin

from accounts.models import Subscriber


class  subscriberAdmin(admin.ModelAdmin):
    list_display=['user','profile_picture']

admin.site.register(Subscriber, subscriberAdmin)