from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.contrib.auth.models import User
from .models import Post, Profile



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'birth_date']
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']