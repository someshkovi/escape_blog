from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('api/', views.apiOverview, name="api-overview"),
    path('api/task-list/', views.taskList, name="task-list"),
    path('api/task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('api/task-create/', views.taskCreate, name="task-create"),
    path('api/task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('api/task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    path('advanced/', views.task_list_advanced, name="task_list_advanced"),
]