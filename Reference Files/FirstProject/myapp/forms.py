from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        fields = "__all__"