from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    created_time = models.DateTimeField(editable=False)
    to_be_completed = models.DateTimeField(blank=True, null=True)
    completed_time = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, related_name='task_author', on_delete=models.CASCADE, null=True, blank=True)
    modified_by = models.ForeignKey(User, related_name='task_modified_by', on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_time = timezone.now()
            # self.author = self.username

        if self.completed:
            self.completed_time = timezone.now()

        if not self.completed:
            self.completed_time = None

        # if self.request:
        #     if self.request.user:
        #         if not self.author:
        #             self.author = self.request.user

        #         if not self.modified_by:
        #             self.modified_by = self.request.user

        # super().save(*args, **kwargs)
        # super().save_model(request, obj, form, change)
        return super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title