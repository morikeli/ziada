from django.urls import path
from . import views

urlpatterns = [
    path('login', views.UserLogin.as_view(), name='login'),
    path('create-new-account/', views.signup_view, name='signup'),
    path('homepage/', views.homepage_view, name='homepage'),
    path('profile', views.userprofile_view, name='user_profile'),

    path('logout/', views.LogoutUser.as_view(), name='logout_user'),
]