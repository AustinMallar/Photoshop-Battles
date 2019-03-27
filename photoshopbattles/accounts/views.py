# Basic login/registration authentication views code referenced from https://github.com/justdjango/Handling-User-Auth

from django.shortcuts import render, redirect
from django.views import generic

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserRegisterForm
from .models import Profile

def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        #Create profile based on the new user.
        new_profile = Profile.objects.create(user=user)
        new_profile.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('/account/two_factor/')

    context = {
        'form': form,
    }
    return render(request, "accounts/signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')

