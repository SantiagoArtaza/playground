from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
# Create your views here.


days_of_week = {
    'monday': "Lunes de garfield ",
    'tuesday': "Martes es goddd",
    'wednesday': "miercoles es el dia del señor",
    'thursday': "Doy clases los jueves no cobro mucho ",
    'friday': "Feliz viernes",
    'saturday': "Sabado de lol",
    'sunday': "domingo de csgo"
}
dayofweek=[{"day": 'monday', "quote": "Lunes de garfield "},
           {"day": 'tuesday', "quote": "Martes es goddd"},
           {"day": 'wednesday', "quote": "miercoles es el dia del señor"},
           {"day": 'thursday', "quote": "Doy clases los jueves no cobro mucho "},
           {"day": 'friday', "quote": "Feliz viernes"},
           {"day": 'saturday', "quote": "Sabado de lol"},
           {"day": 'sunday', "quote": "domingo de csgo"}]

def home(request):
    return render(request, 'quotes/quotes.html',{
        "days": dayofweek
    })
    

def days_week(request, day):
    try:
        quote_text=days_of_week[day.lower()]
        return HttpResponse(quote_text)
    except KeyError:
        raise Http404()

#def days_week_with_number(request, day):

 #  try:
     #  quote_text= days_of_week[list(days_of_week.keys())[day-1]]
    #   return HttpResponse(quote_text)
  # except:
   #      return render(request, 'includes/404.html', status=404)

def  days_week_redirect(request, day):
    try:
        days= list(days_of_week.keys())
        if day> len(days):
            return render(request, 'includes/404.html', status=404)
        
        redirectday= days[day-1]
        redirectpath= reverse("day-of-week", args=[redirectday])
        return HttpResponseRedirect(redirectpath)
    except:
        return render(request, 'includes/404.html', status=404)