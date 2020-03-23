from django import forms
from .models import Feature, FeatureComment


class CreateFeatureReport(forms.ModelForm):
    """
    Form to create a new feature report for the teleporter app
    """

    # Hidden default inputs to initialise the Feature object
    status = forms.CharField(widget=forms.HiddenInput(), initial='Requested')

    # Verify how to initialise vote value. The votes themselves will not be integers but rather count will be based
    # on number of users who have voted. This method should prevent multiple votes by a single user
    # user_votes = forms.IntegerField(widget=forms.HiddenInput(), initial='1')

    class Meta:
        model = Feature
        fields = ('title', 'description')


class FeatureCommentForm(forms.ModelForm):

    class Meta:
        model = FeatureComment
        fields = ('comment',)


class SearchForm(forms.Form):
    query = forms.CharField()
