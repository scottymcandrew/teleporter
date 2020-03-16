from django import forms
from .models import Bug, BugComment


class CreateBugReport(forms.ModelForm):
    """
    Form to create a new bug report for the teleporter app
    """
    SEVERITY_CHOICES = [
        ('Critical', 'Critical'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    severity = forms.ChoiceField(widget=forms.Select, choices=SEVERITY_CHOICES, initial='Low')
    # Hidden default inputs to initialise the Bug object
    status = forms.CharField(widget=forms.HiddenInput(), initial='Open')

    # Verify how to initialise vote value. The votes themselves will not be integers but rather count will be based
    # on number of users who have voted. This method should prevent multiple votes by a single user
    # user_votes = forms.IntegerField(widget=forms.HiddenInput(), initial='1')

    class Meta:
        model = Bug
        fields = ('title', 'description', 'severity')


class BugCommentForm(forms.ModelForm):

    class Meta:
        model = BugComment
        fields = ('comment',)
