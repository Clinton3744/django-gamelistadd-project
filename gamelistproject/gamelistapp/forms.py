from django import forms
from gamelistapp.models import Games


class GameForm(forms.ModelForm):

    class Meta:

        model=Games

        fields='__all__'


