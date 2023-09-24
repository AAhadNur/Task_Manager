from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from userprofile.forms import MyUserCreationForm, UserForm

# Create your views here.


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in ...')
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    return render(request, 'userprofile/login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.save()
            login(request, user)
            messages.success(request, 'User registration done successfully !!')
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'userprofile/register.html', {'form': form})


def userProfile(request, pk):
    user = User.objects.get(id=pk)

    context = {'user': user}
    return render(request, 'userprofile/profile.html', context)
