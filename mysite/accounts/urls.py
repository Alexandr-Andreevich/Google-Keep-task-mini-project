

from django.urls import path
from . import views
from .views import add_task, delete_task, edit_task

urlpatterns = [
    path('', views.page_for_ghost, name='ghost_page'),
    path('users', views.page_for_user, name='user_page'),
    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add/', add_task, name='add_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
]