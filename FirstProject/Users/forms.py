from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from Users.models import Profile

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=254,help_text='Required. Input a valid email address.')
    first_name = forms.CharField(max_length=50,help_text='Required')
    last_name = forms.CharField(max_length=50,help_text='Required')


    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email','password1','password2')




class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=254,help_text='Required. Input a valid email address.')
    first_name = forms.CharField(max_length=50,help_text='Required')
    last_name = forms.CharField(max_length=50,help_text='Required')

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

    

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['images']