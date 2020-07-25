from django import forms

from .models import Register


class ResForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('firstName', 'lastName','email','phoneNumber','height','weight')
        widgets = {
            'firstName': forms.TextInput(attrs={'class': 'main'}),
            'lastName': forms.TextInput(attrs={'class': 'main'}),
            'email': forms.EmailInput(attrs={'class': 'main'}),
            'phoneNumber': forms.NumberInput(attrs={'class': 'main'}),
            'height': forms.NumberInput(attrs={'class': 'main'}),
            'weight': forms.NumberInput(attrs={'class': 'main'}),

        }