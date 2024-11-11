# bookappointment/forms.py
from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'description']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'style': 'width: 80%; padding: 5px; margin-bottom: 10px; border-radius: 5px; border: 1px solid black;'
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'style': 'width: 80%; padding: 5px; margin-bottom: 10px; border-radius: 5px; border: 1px solid black;'
            }),
            'description': forms.TextInput(attrs={
                'style': 'width: 80%; height: 100px; margin-bottom: 20px; padding: 5px; border-radius: 5px; border: 1px solid black;'
            }),
        }

