from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('todo_list/', views.create_task, name='create_task'),
    path('delete_task/<int:id>', views.delete_task, name='delete_task'),
    path('update_task/<int:id>', views.update_task, name='update_task')
]
