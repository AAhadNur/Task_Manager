
from django.urls import path

from userprofile import views

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.registerPage, name='signup'),

    # password reset urls
    path('password-reset/', PasswordResetView.as_view(
        template_name='userprofile/password_reset.html'), name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='userprofile/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='userprofile/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(
        template_name='userprofile/password_reset_complete.html'), name='password_reset_complete'),

    # profile urls
    path('profile/<int:pk>/', views.userProfile, name='profile'),
]
