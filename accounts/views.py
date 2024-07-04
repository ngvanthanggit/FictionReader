from django.shortcuts import render, redirect

import json
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

from .models import User

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages(request, 'Username or Password is wrong!')
        
    context = {}
    return render(request, 'accounts/login_page.html')

def logout_view(request):
    if request.user is None:
        messages(request, 'You have not logged in yet')
    logout(request)
    return redirect('home')


# @require_POST
# def login_view(request):
#     data = json.loads(request.body)
#     username = data.get("login_username")
#     password = data.get("login_password")
    
#     if username == "":
#         print(username, password)
    
#     if username is None or password is None:
#         return JsonResponse({"detail": "Please provide username and password"})
#     user = authenticate(username=username, password=password)
#     if user is None:
#         return JsonResponse({"detail": "Invalid credentials"},
#                             status=400)
#     login(request, user)
#     return JsonResponse({"detail": "Successfully logged in!"})

# def logout_view(request):
#     if not request.user.is_authenticated:
#         return JsonResponse({"detail": "You are not logged in"}, status=400)
#     logout(request)
#     return JsonResponse({"detail": "Successfully logged out!"})

# @ensure_csrf_cookie
# def session_view(request):
#     if not request.user.is_authenticated:
#         return JsonResponse({"isauthenticated": False})
#     return JsonResponse({"isauthenticated": True})

# def whoami_view(request):
#     if not request.user.is_authenticated:
#         return JsonResponse({"isauthenticated": False})
#     return JsonResponse({"username": request.user.username})
