from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User




class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username','email','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class': 'w-full ру-4 px-6 rounded-xl border-2 border-blue-500 p-2 rounded-md w-1/2 focus:border-blue-500 "'

    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Your Email',
        'class': 'w-full ру-4 px-6 rounded-xl border-2 border-blue-500 p-2 rounded-md w-1/2 focus:border-blue-500 "'

    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your Password',
        'class': 'w-full ру-4 px-6 rounded-xl border-2 border-blue-500 p-2 rounded-md w-1/2 focus:border-blue-500 "'

    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password',
        'class': 'w-full ру-4 px-6 rounded-xl border-2 border-blue-500 p-2 rounded-md w-1/2 focus:border-blue-500 "'

    }))


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class': 'w-full ру-4 px-6 rounded-xl border-2 border-blue-500 p-2 rounded-md w-1/2 focus:border-blue-500 "'

    }))
     
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your Password',
        'class': 'w-full ру-4 px-6 rounded-xl border-2 border-blue-500 p-2 rounded-md w-1/2 focus:border-blue-500 "'

    })) 
     
