from django import forms
from .models import Doctor, Patient


class DoctorForm(forms.Form):
    specialization = forms.ChoiceField(choices=Doctor.SPECIALTIES)
    days_of_attendance = forms.MultipleChoiceField(choices=Doctor.DAYS_OF_WEEK)

    doctor_obj = forms.ModelChoiceField(queryset=Doctor.objects.all())


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'birth_date']
