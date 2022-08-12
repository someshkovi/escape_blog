from django.template.defaultfilters import slugify
from django.db import models
from django.urls import reverse
from tinymce import HTMLField


# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=False, unique=True, primary_key=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tutorials:detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class TutorialTopic(models.Model):
    topic_title = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    topic_sub_title = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.SlugField(blank=True, unique=True)
    previous_topic = models.ForeignKey('self', related_name='previous',
                    on_delete=models.SET_NULL, blank=True, null=True)
    next_topic = models.ForeignKey('self', related_name='next',
                    on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.topic_title} > {self.topic_sub_title}'

    def get_edit_url(self):
        return reverse("tutorials:topic-edit", kwargs={"slug": self.slug})

    def get_absolute_url(self):
        return reverse("tutorials:topic-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.topic_title}-{self.topic_sub_title}')
        return super().save(*args, **kwargs)

# class TutorialTopicContent(models.Model):
#     title = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
#     sub_title = models.ForeignKey(TutorialTopic, on_delete=models.CASCADE)
#     content = models.TextField()
