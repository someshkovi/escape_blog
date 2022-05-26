# api/urls.py
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from api.views import TweetList, TweetDetail


urlpatterns = [
    path('auth/', obtain_auth_token),
    path('tweets/', TweetList.as_view()),
    path('tweets/<int:pk>/', TweetDetail.as_view()),
    # path('products/', include('products.urls')),
]