from django.urls import path
from . import views

urlpatterns = [
    path('rating/', views.company_rating_view, name='company_rating'),
]
