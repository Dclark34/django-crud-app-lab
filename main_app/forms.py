from django import forms
from .models import Log

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['date', 'activity']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }