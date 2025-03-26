# ticks/forms.py
from django import forms
from .models import LearnerStatus

class LearnerStatusForm(forms.ModelForm):
    class Meta:
        model = LearnerStatus
        fields = ['learner_id','first_name','status','answer']
