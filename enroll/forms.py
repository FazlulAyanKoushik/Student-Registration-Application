from django.forms import ModelForm
from django import forms
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'gender', 'email', 'password']

        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }