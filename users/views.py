from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import LoginForm, SignupForm, EditProfileForm, UpdateProfileForm


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

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_staff is False and user.is_superuser is False)
@user_passes_test(lambda user: user.students.is_student is True)
def homepage_view(request):

    context = {}
    return render(request, 'students/homepage.html', context)

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_staff is False and user.is_superuser is False)
@user_passes_test(lambda user: user.lecturers.is_student is True)
def userprofile_view(request):
    editprofile_form = EditProfileForm(instance=request.user.students)
    updateprofile_form = UpdateProfileForm(instance=request.user.students)

    if request.method == 'POST':
        editprofile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.students)
        updateprofile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.students)

        if updateprofile_form.is_valid():
            form = updateprofile_form.save(commit=False)
            form.is_student = True
            form.save()

            messages.success(request, 'Profile updated successfully!')
            return redirect('user_profile')
        
        elif editprofile_form.is_valid():
            editprofile_form.save()
            messages.info(request, 'Profile pic updated successfully!')
            return redirect('user_profile')


    context = {'edit_profile': editprofile_form, 'update_profile': updateprofile_form,}
    return render(request, 'students/profile.html', context)


class LogoutUser(LogoutView):
    template_name = 'students/logout.html'