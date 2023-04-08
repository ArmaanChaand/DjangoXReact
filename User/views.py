from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth import login, logout, authenticate
from .forms import NewUserForm
from Home.models import  Note
from .models import CustomUser
import json
# Create your views here.

def UserData(request):
    user = request.user
    data = {}
    user_data = {}
    if user.is_authenticated:
        data['success'] = True
        user_data['is_Authenticated'] = True
        user_data['username'] = user.username
        user_data['my_notes'] = user.my_notes.all().count()
    else:
        data['success'] = False
        user_data['is_Authenticated'] = False
    data['user_data'] = user_data
    return JsonResponse(data)

def NewUser(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            newUser = form.save()
            login(request, newUser)
            user_data = {}
            user_data['is_Authenticated'] = True
            user_data['username'] = request.POST.get('username')
            user_data['my_notes'] = 0
            data = {
                "success": True,
                "authenticated": True,
                "user_data":user_data
            }
            return JsonResponse(data)
        else:
            data = {
                "success": False,
                "error": True,
                "errors": form.errors
            }
            return JsonResponse(data)

def LoginUser(request):
    if request.method == "POST":
        POST_DATA = json.loads(request.body)
        username = POST_DATA["username"]
        password = POST_DATA["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            data = {
                "authenticated": True,
            }
            user_data = {}
            user_data['is_Authenticated'] = True
            user_data['username'] = user.username
            user_data['my_notes'] = user.my_notes.all().count()
            data['user_data'] = user_data
            return JsonResponse(data)
        else:
            data = {
                "authenticated": False,
                "errors": "invalid Credentials!"
            }
            return JsonResponse(data)

def LogoutUser(request):
    data = {}
    if request.user.is_authenticated:
        logout(request)
        data['success'] = True
    else:
        data['success'] = False
        data['error'] = 'user_unAuthenticated'
    return JsonResponse(data)

def get_csrf_token(request):
    token = get_token(request)
    data = {
        "csrf_token": token
    }
    return JsonResponse(data)

def getAllUser(request):
    allUsers = []
    for user in  CustomUser.objects.all():
        user_obj = {
            'username':  user.username
        }
        allUsers.append(user_obj)
    data = {
        'allUsers': allUsers
    }
    return JsonResponse(data)