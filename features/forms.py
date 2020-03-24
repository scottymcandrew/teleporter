from django import forms
from .models import Feature, FeatureComment


class CreateFeatureReport(forms.ModelForm):
    """
    Form to create a new feature report for the teleporter app
    """

    # Hidden default inputs to initialise the Feature object
    status = forms.CharField(widget=forms.HiddenInput(), initial='Requested')
    # Since this form is for users, we default the category to user-requested.
    category = forms.CharField(widget=forms.HiddenInput(), initial='User-Requested')

    class Meta:
        model = Feature
        fields = ('title', 'description')


class FeatureCommentForm(forms.ModelForm):

    class Meta:
        model = FeatureComment
        fields = ('comment',)


class SearchForm(forms.Form):
    query = forms.CharField()
