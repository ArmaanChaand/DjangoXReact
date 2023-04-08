"""FirstIntegration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home.views import NewNoteApi, deleteNoteApi, getAllNotes
from User.views import NewUser, LoginUser, UserData, LogoutUser, get_csrf_token, getAllUser
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    #API
    path('api/user/', UserData, name="user-data-api"),
    path('api/register/', NewUser, name="register-api"),
    path('api/login/', LoginUser, name="login-api"),
    path('api/logout/', LogoutUser, name="logout-api"),
    path('api/allnotes/', getAllNotes, name="all-note-api"),
    path('api/allusers/', getAllUser, name="all-user-api"),
    path('api/newNote/', NewNoteApi, name="new-note-api"),
    path('api/deleteNote/', deleteNoteApi, name="delete-note-api"),
    path('api/getToken/', get_csrf_token, name="get-csrf-api"),

    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('<path:path>', TemplateView.as_view(template_name='index.html'), name='index'),
]
