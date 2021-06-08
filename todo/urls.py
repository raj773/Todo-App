
from django.contrib import admin
from django.urls import path
from . import views
from todo.views import add_todo,logout_view,change_todo,delete_todo

urlpatterns = [
    path('', views.home, name='home'),
    path('login_view/', views.login_view, name='login_view'),
    path('signup/', views.signup, name='signup'),
    path('add-todo/' , add_todo,name='add_todo'),
    path('logout_view/' ,logout_view,name='logout_view'),
    path('delete-todo/<int:id>' , delete_todo,name='delete-todo'), 
    path('change-status/<int:id>/<str:status>' , change_todo,name='change_todo'),
 
]
