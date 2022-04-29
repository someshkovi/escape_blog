from django.urls import path
from .views import TweetListView, TweetCreateView, index

app_name = 'tweets'
urlpatterns = [
    path('new/', TweetCreateView.as_view(), name='tweet_new'),
    path('list/', TweetListView.as_view(), name='home'),
    path('', index, name='index')
]