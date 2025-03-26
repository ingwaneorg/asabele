# ticks/forms.py
from django import forms
from .models import LearnerStatus

class LearnerStatusForm(forms.ModelForm):
    class Meta:
        model = LearnerStatus
        fields = ['first_name', 'status', 'answer']

    # Optional: Add custom validation for required fields if needed
    first_name = forms.CharField(max_length=15, required=True)  # Make sure it's required
