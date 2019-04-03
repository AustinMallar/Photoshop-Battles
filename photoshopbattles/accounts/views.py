# Basic login/registration authentication views code referenced from https://github.com/justdjango/Handling-User-Auth

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserRegisterForm,EditProfileForm
from django.contrib.auth.models import User
from .models import Profile
from application.models import Post

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

def profile_view(request, username):
    user_object = get_object_or_404(User, username=username)
    profile = user_object.profile
    posts_by_user = Post.objects.filter(user=user_object)
    context = {
        'user_object': user_object,
        'profile': profile,
        'posts_by_user': posts_by_user
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def profile_edit_view(request):
    form = EditProfileForm(request.POST or None, request.FILES or None)
    user = request.user
    if form.is_valid():
        
        bio = form.cleaned_data.get('bio')
        image = form.cleaned_data.get('image')
        user.profile.bio=bio
        user.profile.image=image
        user.profile.save()
       
        return redirect(f'/profile/{user.username}')
    
    context = {
        'form': form,
    }
    return render(request, "accounts/edit_profile.html", context)