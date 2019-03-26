from django.contrib import admin
from django.urls import path,include
from .views import register_view,logout_view

urlpatterns = [
    path('register/', register_view),
    path('logout/', logout_view)
]

