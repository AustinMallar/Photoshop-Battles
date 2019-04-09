from django.urls import path,include
from . import views
from .views import leaderboard_view, profile_view, new_post

app_name = 'application'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('leaderboard', leaderboard_view),
    path('profile', profile_view),
    path('new_post', new_post),
]