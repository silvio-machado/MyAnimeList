from django import forms
from mal.models import Animes

class NewAnimeForm(forms.ModelForm):
    class Meta():
        model = Animes
        fields = '__all__'
