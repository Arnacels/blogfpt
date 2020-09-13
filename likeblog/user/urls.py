from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/profile/', views.cabinet, name="profile"),
    path('accounts/signup/', views.signup_view, name="signup"),
    path('accounts/profile/logout/', views.logout_user, name='profile_logout'),
]