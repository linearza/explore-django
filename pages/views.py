from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
  print(request.user, args, kwargs)
  return HttpResponse("<h1>Hello world</h1>")

def contact_view(*args, **kwargs):
  return HttpResponse("<h1>Contact us</h1>")