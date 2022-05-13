import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from tinymce import HTMLField

from accounts.models import Subscriber

User = get_user_model()

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.username} viewed {self.post.title}'

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('POST', on_delete=models.CASCADE)

class Category(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.username} comment on {self.post.title}'

class Post(models.Model):
    title = models.CharField(max_length=50)
    overview = models.TextField()
    timestamp = models.DateTimeField(blank=True, null=True, editable=False)
    content = HTMLField()
    # comment_count = models.IntegerField(default=0)
    # view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    thumbnail = models.ImageField(blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    featured = models.BooleanField(default=False)
    read_time = models.IntegerField(help_text='Read time in minutes', default=10, editable=True)
    previous_post = models.ForeignKey('self', related_name='previous',
                    on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next',
                 on_delete=models.SET_NULL, blank=True, null=True)
    publish = models.BooleanField(default=True, editable=True)
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    pub_date = models.DateTimeField(blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        if self.publish and not self.pub_date:
            self.pub_date = timezone.now()
        if self.pub_date and not self.publish:
            self.pub_date = None
        self.timestamp = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.title} by {self.author}'

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        if not self.pub_date:
            return False
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_date <= now

    def was_modified_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.timestamp <= now

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"id": self.id})

    def get_update_url(self):
        return reverse("post-update", kwargs={
            "id": self.id
        })

    def get_delete_url(self):
        return reverse("post-delete", kwargs={
            "id": self.id
        })

    @property
    def get_comments(self):
        return self.comments.order_by('-timestamp')

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()

    @property
    def like_count(self):
        return PostLike.objects.filter(post=self).count()
