from django.shortcuts import render
from django.http import HttpResponse
from.models import Room

# Create your views here.

def index(request):
    rooms=Room.objects.all()
    return render(request,'index.html',{'rooms':rooms})

def about(request): 
    return HttpResponse(request,'about.html')
