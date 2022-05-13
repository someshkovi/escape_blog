from django.contrib.auth.models import User
from django.test import TestCase
from django.db.models import Max

from posts.models import Post
from accounts.models import Subscriber

class PostModelTests(TestCase):
    def setUp(self):
        user=User.objects.create_user('foo3', password='bar')
        # user.is_superuser=True
        # user.is_staff=True
        user.save()
        a1 = Subscriber.objects.create(user=user)
        a1.save()

        p1 = Post.objects.create(
            title='title',
            overview='overview',
            content='content',
            author=a1,
            # categories = [cat],
            featured=True,
            publish=True)
        p1.save()
        Post.objects.create(
            title='title2',
            overview='overview2',
            content='content2',
            author=a1,
            # categories = [cat],
            featured=False,
            publish=True
        )
        Post.objects.create(
            title='title2',
            overview='overview2',
            content='content2',
            author=a1,
            # categories = [cat],
            featured=False,
            publish=False
        )
        # Category.objects.create(title='category1')
        # cat = Category.objects.get(title='category1')
        # p1.categories.set([cat])              # to be checked on how to add many to many fields

    def test_post_creation(self):
        p = Post.objects.get(title='title')
        self.assertEqual(p.overview, 'overview')

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object_list'].count(), 1)
        self.assertEqual(response.context['latest'].count(), 2)

    def test_valid_post_page(self):
        p = Post.objects.get(title='title')
        response = self.client.get(f'/post/{p.id}/')
        self.assertEqual(response.status_code, 200)

    def test_invalid_post_page(self):
        max_id = Post.objects.all().aggregate(Max('id'))['id__max']
        response = self.client.get(f'/post/{max_id+1}/')
        self.assertEqual(response.status_code, 404)
