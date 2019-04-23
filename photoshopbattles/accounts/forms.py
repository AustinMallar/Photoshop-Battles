# Basic login/registration authentication forms code referenced from https://github.com/justdjango/Handling-User-Auth

from django import forms
from .models import Profile
from django.contrib.auth import (
    authenticate,
    get_user_model
)

User = get_user_model()

# EditProfileForm allows the user to edit their bio and image
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image',
            'bio',
        ]

    def clean(self, *args, **kwargs):
        image = self.cleaned_data.get('image')
        bio = self.cleaned_data.get('bio')
        
        return super(EditProfileForm, self).clean(*args, **kwargs)

# UserRegisterForm allows the user to register with
# a username, email address and password
class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)
