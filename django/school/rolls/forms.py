from tkinter import Widget
from django import forms
from .models import Student


class NameForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'gender',
            'date',
            'mopile',
            'email',
            'gpa',
            'idenNum',
            'status',
            'level',
            'department'
        ]
        Widget = {
            'name': forms.TextInput(),
            'gender': forms.Select(),
            'date': forms.DateField(),
            'mopile': forms.NumberInput(),
            'email': forms.EmailField(),
            'gpa': forms.NumberInput(),
            'idenNum': forms.NumberInput(),
            'status': forms.Select(),
            'level': forms.Select(),
            'department': forms.Select()
        }
