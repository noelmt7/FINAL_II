from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse

def Booking(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())