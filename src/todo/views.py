from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-create/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    # print(request.user)
    tasks = Task.objects.all().filter(author=request.user).order_by('-created_time')
    serializers = TaskSerializer(tasks, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializers = TaskSerializer(tasks, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def taskCreate(request):
    serializers = TaskSerializer(data=request.data)

    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializers = TaskSerializer(instance=task, data=request.data)

    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Task Successfully Deleted!')

@login_required(login_url='/admin/login/')
def task_list(request):
    return render(request, 'todo/list.html')

@login_required(login_url='/accounts/login/')
def task_list_advanced(request):
    return render(request, 'todo/list_advanced.html')