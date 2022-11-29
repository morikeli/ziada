from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import LoginForm, SignupForm


class UserLogin(LoginView):
    authentication_form = LoginForm
    template_name = 'users/login.html'


def signup_view(request):
    form = SignupForm()


    context = {'signup_form': form}
    return render(request, 'users/signup.html', context)

def homepage_view(request):

    context = {}
    return render(request, 'users/homepage.html', context)


def userprofile_view(request):

    context = {}
    return render(request, 'users/profile.html', context)

class LogoutUser(LogoutView):
    template_name = 'users/logout.html'