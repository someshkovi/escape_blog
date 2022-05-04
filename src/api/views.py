# api/views.py
from rest_framework import generics
from tweets.models import Tweet
from tweets.serializers import TweetSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

class TweetList(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer