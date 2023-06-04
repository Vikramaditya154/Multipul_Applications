from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app3(request):
    return HttpResponse('<h1> app3 is created </h1>')
def app3_html(request):
    return render(request,'app3.html')