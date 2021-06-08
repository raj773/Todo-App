from rest_framework import generics
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Task

class TaskCreateApi(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskApi(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer   

class TaskUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDeleteApi(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer