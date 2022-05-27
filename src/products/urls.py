from django.urls import path
from .views import index, ProductList, ProductUpdateAPIView, ProductDetail

app_name = 'products'
urlpatterns = [
    path('', index, name='index'),
    # path('', ProductList.as_view(), name='products-list'),
    # path("<int:pk>/", ProductDetail.as_view(), name='product-detail'),
    # path("<int:pk>/update/", ProductUpdateAPIView.as_view(), name='product-edit')
]