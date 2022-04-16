from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts import views

urlpatterns = [
    path('', views.index),
    path('blog/', views.blog, name='post-list'),
    path('post/<id>/', views.post, name='post-detail'),
    path('search/', views.search, name='search'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)