from django import forms
from .models import Doctor, Patient


class DoctorModelForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = '__all__'


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
