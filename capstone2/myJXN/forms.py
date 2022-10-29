
from django import forms
from .models import Type, Entry
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
# create a ModelForm
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = "__all__"
        widgets = {'lat': forms.HiddenInput(), 'lon': forms.HiddenInput()}
        


class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']