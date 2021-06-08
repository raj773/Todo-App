from django.urls import path
from .api import TaskCreateApi,TaskApi,TaskUpdateApi,TaskDeleteApi

urlpatterns = [
    path('task',TaskApi.as_view()),
    path('task/create',TaskCreateApi.as_view()),
    path('task/<int:pk>',TaskUpdateApi.as_view()),
    path('task/<int:pk>/delete',TaskDeleteApi.as_view()),
]