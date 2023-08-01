from django import forms
from new.models import student


class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['firstname', 'lastname', 'email']
