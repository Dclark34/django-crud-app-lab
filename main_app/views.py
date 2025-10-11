from django.shortcuts import render
from django.http import HttpResponse

#homepage
def home(request):
    return HttpResponse('<h1>Welcome to The National Parks Tracker!</h1>')

#about route
def about(request):
    return render(request, 'about.html')
