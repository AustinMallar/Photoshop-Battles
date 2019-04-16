from django.urls import path,include
from .views import IndexView,leaderboard_view, profile_view, new_post, delete_post, delete_reply, like_reply, unlike_reply

app_name = 'application'

urlpatterns = [
    path('', IndexView, name='index'),
    path('leaderboard', leaderboard_view),
    path('profile', profile_view),
    path('new_post', new_post),
    path('delete_post/<int:id>',delete_post),
    path('delete_reply/<int:id>',delete_reply),
    path('like_reply/<int:id>',like_reply),
    path('unlike_reply/<int:id>',unlike_reply)
]