from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_list, name='resume_list'),
    path('create/', views.resume_create, name='resume_create'),
    path('update/<int:pk>/', views.resume_update, name='resume_update'),
    path('delete/<int:pk>/', views.resume_delete, name='resume_delete'),
]