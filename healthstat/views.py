from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

from .forms import SignUpForm
from start.models import UserProfile


def index(request):
    if request.user.is_authenticated:
        return redirect('/start/')
    else:
        return render(request, 'index.html')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = True
                user.save()
                p = UserProfile(
                    usrId=user.id
                )
                p.save()
                login(request, user)

            return redirect('/')
        else:
            form = SignUpForm()

        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('/start/')


def logoutView(request):
    logout(request)
    return redirect('/')