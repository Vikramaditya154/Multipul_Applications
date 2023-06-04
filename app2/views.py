from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Start(request):
    return HttpResponse('<center><h1>stating new views </h1></center>')
def second(request):
    return render(request,'start.html')