from django import forms

from .models import UserChoice

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = UserChoice
        fields = ['choice']
