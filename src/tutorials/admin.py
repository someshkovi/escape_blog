from django.contrib import admin
from .models import Tutorial, TutorialTopic
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
    list_display= ('title',)
    prepopulated_fields= {'slug':('title',)}

admin.site.register(Tutorial, TutorialAdmin)

class TutorialTopicAdmin(admin.ModelAdmin):
    list_display= ('topic_title','topic_sub_title', 'slug')
    prepopulated_fields= {'slug':('topic_title','topic_sub_title')}

    # def get_title(self, obj):
    #     return obj.topic_title

admin.site.register(TutorialTopic, TutorialTopicAdmin)