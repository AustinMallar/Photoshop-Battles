from django.http import HttpResponseRedirect,HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Post, Reply, Liked, Favourite
from .forms import NewPost, NewReply
from accounts.models import Profile

def IndexView(request):

    if request.method =='POST':
        reply_form = NewReply(request.POST or None, request.FILES or None)
        user = request.user

        if reply_form.is_valid():
            
            title = reply_form.cleaned_data.get('title')
            image = reply_form.cleaned_data.get('image')
            postID = request.POST.get("postID")
            post=Post.objects.filter(id=postID)[0]
            Reply.objects.create(
                title=title,
                image=image,
                user=user,
                post_replying_to=post,
                pub_date = timezone.now(),
            )
        
            return HttpResponseRedirect('/')

    else:
        context = {}
        context['reply_form'] = NewReply()
        latest_posts = Post.objects.all().order_by('-pub_date')

        # Pagination code referenced from https://docs.djangoproject.com/en/2.2/topics/pagination/
        paginator = Paginator(latest_posts, 5)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        context['posts'] = posts

        return render(request, 'application/home.html', context)

def leaderboard_view(request):
    context = {}
    latest_replies = Reply.objects.all().order_by('-pub_date')[:3]
    context['replies'] = latest_replies
    latest_Profiles = Profile.objects.all()[:3]
    context['profiles'] = latest_Profiles
    return render(request, 'application/leaderboard.html', context)

def profile_view(request):
    return render(request, 'application/profile.html')

def new_post(request):
    form = NewPost(request.POST or None, request.FILES or None)
    user = request.user

    if form.is_valid():
        
        title = form.cleaned_data.get('title')
        image = form.cleaned_data.get('image')
        Post.objects.create(
            title=title,
            image=image,
            user=user,
            pub_date = timezone.now(),
        )
       
        return redirect(f'/')
    
    context = {
        'form': form,
    }

    return render(request, 'application/new_post.html', context)

def delete_post(request,id):
    user = request.user
    post = get_object_or_404(Post, pk=id)
    if user == post.user:
        post.delete()
        return HttpResponseRedirect('/')    
    else:
        return HttpResponseRedirect('/')

def delete_reply(request,id):
    user = request.user
    reply = get_object_or_404(Reply, pk=id)
    if user == reply.user:
        reply.delete()
        return HttpResponseRedirect('/')    
    else:
        return HttpResponseRedirect('/')
    
def like_reply(request, id):
    user = request.user
    reply = get_object_or_404(Reply, pk=id)
    Liked.objects.create(
        user = user,
        reply = reply,
    )
    return JsonResponse({'likes': int(reply.liked_set.count())})

def unlike_reply(request, id):
    user = request.user
    reply = get_object_or_404(Reply, pk=id)
    liked = reply.liked_set.get(user=user)
    if liked:
        liked.delete()
        return JsonResponse({'likes': int(reply.liked_set.count())})
    else:
        return JsonResponse({'likes':int(reply.liked_set.count())})

def favourite_reply(request, id):
    user = request.user
    reply = get_object_or_404(Reply, pk=id)
    Favourite.objects.create(
        user = user,
        reply = reply,
    )
    return HttpResponse(200)

def unfavourite_reply(request, id):
    user = request.user
    reply = get_object_or_404(Reply, pk=id)
    favourite = reply.favourite_set.get(user=user)
    if favourite:
        favourite.delete()
        return HttpResponse(200)    
    else:
        return HttpResponseRedirect(301)