from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.

def home(request):
  date_today = date.today()
  stack= [{"id": 1, "name": "Python"}, {"id": 2, "name": "Django"}, {"id": 3, "name": "JavaScript"}, {"id": 4, "name": "React"}, {"id": 5, "name": "HTML"}, {"id": 6, "name": "CSS"}]

  return render(request,'landing/landing.html',{
       "name": "Sarie",
        "age": 22,
        "date": date_today,
        "stack": stack
   })
  
def stack(request, stack_name):
  return HttpResponse(f"Stack: {stack_name}")

