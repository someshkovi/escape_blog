from ast import Sub
from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User

from tweets.models import Tweet
from posts.models import Post
from accounts.models import Subscriber

class UserSerializer(serializers.ModelSerializer):
    tweets = serializers.PrimaryKeyRelatedField(many=True, queryset=Tweet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'products', 'tweets']

class AuthorSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    class Meta:
        model = Subscriber
        fields = '__all__'