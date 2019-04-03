from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Post,Reply

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