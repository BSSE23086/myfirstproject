from django import forms
from .models import Room, User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # Removed 'password1' and 'password2' - Django handles these automatically!
        fields = ['name', 'username', 'email'] 

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']