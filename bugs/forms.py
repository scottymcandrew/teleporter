from django import forms
from .models import Bug


class CreateBugReport(forms.ModelForm):
    """
    Form to create a new bug report for the teleporter app
    """
    class Meta:
        model = Bug
        fields = ('title', 'description', 'severity')
