from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import Http404, HttpResponse
# Create your views here.

def login(request):
    return render(request, 'login.html')