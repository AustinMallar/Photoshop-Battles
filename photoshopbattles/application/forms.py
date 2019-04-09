# Basic login/registration authentication forms code referenced from https://github.com/justdjango/Handling-User-Auth

from django import forms
from .models import Post
from .models import Reply
from django.contrib.auth import (
    authenticate,
    get_user_model
)

User = get_user_model()


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'image',
        ]

    def clean(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        image = self.cleaned_data.get('image')
        
        return super(NewPost, self).clean(*args, **kwargs)


class NewReply(forms.ModelForm):
    class Meta:
        model = Reply
        fields = [
            'title',
            'image',
        ]

    def clean(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        image = self.cleaned_data.get('image')
        
        return super(NewReply, self).clean(*args, **kwargs)