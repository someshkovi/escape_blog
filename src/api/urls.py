# api/urls.py
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from api.views import TweetList, TweetDetail, api_root
from accounts.views import UserList, UserDetail
from products.views import ProductList, ProductUpdateAPIView, ProductDetail

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('auth/', obtain_auth_token),
    path('tweets/', TweetList.as_view()),
    path('tweets/<int:pk>/', TweetDetail.as_view()),
    # path('products/', include('products.urls')),
    path('users/', UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('products/', ProductList.as_view(), name='products-list'),
    path("products/<int:pk>/", ProductDetail.as_view(), name='product-detail'),
    path("products/<int:pk>/update/", ProductUpdateAPIView.as_view(), name='product-edit')
])