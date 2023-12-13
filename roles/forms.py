from typing import Any
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify

class CustomUserCreationForm(UserCreationForm):

    def save(self, commit = True) -> Any:
       user = super().save(commit=False)
       username = slugify(self.cleaned_data['email'].split('@')[0])
       user.username = username
       if commit:
            user.save()
       return user
    

    class Meta(UserCreationForm.Meta):
        model = User
        exclude = ['username']
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', 'role')