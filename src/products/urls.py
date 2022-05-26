from django.urls import path
from .views import index, ProductList, ProductUpdateAPIView, ProductDetail, UserList, UserDetail

app_name = 'products'
urlpatterns = [
    path('all/', index, name='index'),
    path('', ProductList.as_view(), name='product-list'),
    path("<int:pk>/", ProductDetail.as_view(), name='product-detail'),
    path("<int:pk>/update/", ProductUpdateAPIView.as_view(), name='product-edit'),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]