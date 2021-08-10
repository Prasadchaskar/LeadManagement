
from django.forms import ModelForm
from . models import Lead
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Agent

class LeadgenerationForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['client_Name','business_Type','mobile_No','email','address','requirement','department','agent_id']
    
class UpdateStatus(ModelForm):
     class Meta:
        model = Lead
        fields = ['status']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']