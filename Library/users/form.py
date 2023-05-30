from django import forms
from django.db.models import fields
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User, UserManager


class UserForm(UserCreationForm):
    email = models.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
 
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
