from django.contrib import admin
from django.urls import path,include
from .views import register_view,logout_view,profile_view,profile_edit_view

urlpatterns = [
    path('account/register/', register_view),
    path('account/logout/', logout_view),
    path('profile/<str:username>',profile_view),
    path('account/edit-profile',profile_edit_view)
]

