from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.user_register_view, name='register'),
]