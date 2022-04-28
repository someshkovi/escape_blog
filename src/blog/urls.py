from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts import views

urlpatterns = [
    path('', views.index),
    path('blog/', views.blog, name='post-list'),
    path('search/', views.search, name='search'),
    path('create/', views.post_create, name='post-create'),
    path('post/<id>/', views.post, name='post-detail'),
    path('post/<id>/update/', views.post_update, name='post-update'),
    path('post/<id>/delete/', views.post_delete, name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('tweet/', include('tweets.urls')),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

admin.site.site_header  =  "Escape admin"
admin.site.site_title  =  "Escape admin site"
admin.site.index_title  =  "Escape Admin"
