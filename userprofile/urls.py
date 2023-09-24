
from django.urls import path

from userprofile import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.registerPage, name='signup'),
]
