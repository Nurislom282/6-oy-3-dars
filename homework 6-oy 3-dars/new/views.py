from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.
def mainpage(request: WSGIRequest):
    return render(request,'index.html')