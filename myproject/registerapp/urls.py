from django.urls import path
from .views import register, success_view  # Import success_view

urlpatterns = [
    path('', register, name='register'),
    path('success/', success_view, name='success'),  # Define success view path
]