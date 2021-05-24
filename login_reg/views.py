from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import creds
from django.contrib.auth.models import User, auth

def registration(request):
    if request.method == 'POST':
        username = request.POST['Username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
    
        user =  User.objects.create_user(username=username, password=password1, email=email)
        user.save()
        return render(request, 'home.html')
    else:
        return render(request, 'registration.html', {'creds1':creds})