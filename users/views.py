from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import LoginForm, SignupForm


class UserLogin(LoginView):
    authentication_form = LoginForm
    template_name = 'students/login.html'


def signup_view(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = new_user.first_name + ' ' + new_user.last_name
            new_user.save()
            messages.success(request, f'New account for "{new_user.username}" created successfully!')
            return redirect('user_profile')

    context = {'signup_form': form}
    return render(request, 'students/signup.html', context)

def homepage_view(request):

    context = {}
    return render(request, 'students/homepage.html', context)


def userprofile_view(request):

    context = {}
    return render(request, 'students/profile.html', context)

class LogoutUser(LogoutView):
    template_name = 'students/logout.html'