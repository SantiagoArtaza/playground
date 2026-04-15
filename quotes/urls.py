from django.urls import path
from . import views

urlpatterns = [
    path ('home', views.home, name="quotes"),
    path('<int:day>', views.days_week_redirect, name="day-redirect"),    
    path('<str:day>', views.days_week , name="day-of-week"),    
   
    
    
]
