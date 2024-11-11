# services/forms.py
from django import forms
from .models import Service, ServiceRequest

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'file', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'style': 'background-color: transparent; border: 1px solid black; padding: 8px; border-radius: 10px; margin-bottom: 10px; width: 80%'}),
            'description': forms.Textarea(attrs={'style': 'background-color: transparent; border: 1px solid black; border-radius: 10px; padding: 8px; margin-bottom: 20px; width: 80%'}),
            'file': forms.ClearableFileInput(attrs={'style': 'padding: 8px; border-radius: 10px; margin-bottom: 10px;'}),
            'image': forms.ClearableFileInput(attrs={'style': 'padding: 8px; border-radius: 10px;'}),
        }

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_description', 'request_file']
        widgets = {
            'request_description': forms.Textarea(attrs={
                'style': 'width: 100%; color: black; margin-top: 20px; padding: 10px; border: 1px solid black; border-radius: 4px;',
                'placeholder': 'Enter the description of your request...',
                'rows': 4  # Optional: Specify the number of rows
            }),
            'request_file': forms.ClearableFileInput(attrs={
                'style': '''
                                display: block;
                                width: 100%;
                                max-width: 300px;
                                padding: 12px;
                                border: 2px solid #e0e0e0;
                                border-radius: 8px;
                                background-color: #f9f9f9;
                                color: black;
                                margin-top: 20px;
                                font-size: 16px;
                                transition: border-color 0.3s ease;
                            ''',
                'onfocus': "this.style.borderColor='#007bff'",
                'onblur': "this.style.borderColor='#e0e0e0'"
            }),

        }