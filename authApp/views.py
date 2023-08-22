from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View

class CustomLognView(LoginView):
    redirect_authenticated_user = True
    template_name = 'auth/login.html'
    next_page = '/'
    # form_class = LoginForm
class CustomLogoutView(LogoutView):
    template_name = 'auth/logout.html'