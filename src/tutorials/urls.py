from django.urls import path
from . import views

app_name = 'tutorials'
urlpatterns = [
    path('', views.TutorialsListView.as_view(), name='list'),
    path('<slug:slug>', views.TutorialsTopicListView.as_view(), name='detail'),
    path('create/tutorial', views.TutorialsCreateview.as_view(), name='create'),
    path('<slug:slug>/add', views.TutorialsTopicCreateView.as_view(), name='topic-add'),
    path('topic/add', views.TutorialsTopicCreateView.as_view(), name='topic-create'),
    path('view/<slug:slug>', views.TutorialsTopicDetailView.as_view(), name='topic-detail'),
    path('edit/<slug:slug>', views.TutorialsTopicUpdateView.as_view(), name='topic-edit'),
]