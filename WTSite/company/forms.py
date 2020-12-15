from django import forms
from .models import Company


class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
