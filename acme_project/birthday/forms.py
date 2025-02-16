from django import forms
from .models import Birthday, Congratulation

class BirthdayForms(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = ['first_name', 'last_name', 'birthday', 'image', 'author', 'tags']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

class CongratulationForm(forms.ModelForm):
    class Meta:
        model = Congratulation
        fields = ['text']
