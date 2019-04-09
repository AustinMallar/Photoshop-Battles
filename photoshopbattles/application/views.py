from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Post,Reply
from .forms import NewPost

class IndexView(generic.ListView):
    template_name = 'application/home.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:20]

def leaderboard_view(request):
    return render(request, 'application/leaderboard.html')

def profile_view(request):
    return render(request, 'application/profile.html')

def new_post(request):
    form = NewPost(request.POST or None, request.FILES or None)
    user = request.user

    if form.is_valid():
        
        title = form.cleaned_data.get('title')
        image = form.cleaned_data.get('image')
        post = Post.objects.create(
            title=title,
            image=image,
            user=user,
            pub_date = timezone.now(),
        )
       
        return redirect(f'/home')
    
    context = {
        'form': form,
    }

    return render(request, 'application/new_post.html', context)