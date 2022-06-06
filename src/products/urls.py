from django.urls import path
from .views import index, ProductList, ProductUpdateAPIView, ProductDetail, search_result_by_category, search_result_by_products_search_result_keywords

app_name = 'products'
urlpatterns = [
    path('', index, name='index'),
    path('category:<category>/', search_result_by_category),
    path('search:<search_keyword>/', search_result_by_products_search_result_keywords),
    # path('', ProductList.as_view(), name='products-list'),
    # path("<int:pk>/", ProductDetail.as_view(), name='product-detail'),
    # path("<int:pk>/update/", ProductUpdateAPIView.as_view(), name='product-edit')
]