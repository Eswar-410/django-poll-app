from django import forms

from .models import CreateForm


class ValidForm(forms.ModelForm):
    class Meta:
        model = CreateForm
        fields = '__all__'
