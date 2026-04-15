from django.urls import path
from . import  views

urlpatterns = [
    path('home', views.home, name='home'),
    path('stack/<str:stack_name>', views.stack, name='stack')
]
