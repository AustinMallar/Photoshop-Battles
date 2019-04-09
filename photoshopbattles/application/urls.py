from django.urls import path,include
from .views import IndexView,leaderboard_view, profile_view, new_post

app_name = 'application'

urlpatterns = [
    path('', IndexView, name='index'),
    path('leaderboard', leaderboard_view),
    path('profile', profile_view),
    path('new_post', new_post),
    
]