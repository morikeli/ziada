from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages


class UserLogin(LoginView):
    template_name = 'students/login.html'


def signup_view(request):

    context = {}
    return render(request, 'students/signup.html', context)

def homepage_view(request):

    context = {}
    return render(request, 'students/homepage.html', context)


class LogoutUser(LogoutView):
    template_name = 'students/logout.html'