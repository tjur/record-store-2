# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print username
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login_user(request, user)
                return redirect(index)
            else:
                return render(request, "login.html", context={"error": "Konto jest nieaktywne"})
        else:
            return render(request, "login.html", context={"error": "Niepoprawne dane"})
    else:
        return render(request, "login.html")

def logout(request):
    logout_user(request)
    return redirect(index)

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        errors = []
        if not username:
            errors.append("Nie podano nazwy użytkownika")
        elif User.objects.filter(username=username).exists():
            errors.append("Podana nazwa użytkownika jest zajęta")

        if not first_name:
            errors.append("Nie podano imienia")
        if not last_name:
            errors.append("Nie podano nazwiska")

        if not email:
            errors.append("Nie podano adresu email")
        elif User.objects.filter(email=email).exists():
            errors.append("Istnieje już użytkownik o podanym adresie email")

        if not password:
            errors.append("Nie podano hasła")
        elif len(password) < 5:
            errors.append("Za krótkie hasło")
        elif not password_confirm:
            errors.append("Nie podano potwierdzenia hasła")
        elif password != password_confirm:
            errors.append("Podane hasła nie zgadzają się")

        if errors:
            return render(request, "register.html", context={"errors": errors})
        else:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            user = authenticate(username=username, password=password)
            login_user(request, user)
            return redirect(index)
    else:
        return render(request, "register.html")

def contact(request):
    return render(request, "contact.html")