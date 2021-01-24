from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import UserProfile

class CreateUserForm(UserCreationForm, ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('identification', 'phone', 'location',)

class UserProfileExtraInfoForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic', 'phone', 'location',)
        # fields = '__all__'