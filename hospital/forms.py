from django import forms
from .models import Doctor


class DoctorForm(forms.Form):
    specialization = forms.ChoiceField(choices =(('Allergology&Immunology', 'Allergology&Immunology'),
                                        ('Infectious_diseases', 'Infectious_diseases'),
                                        ('Dermatology', 'Dermatology'),
                                        ('Internal_Medicine', 'Internal_Medicine'),
                                        ('Endocrinology', 'Endocrinology'),
                                        ('Gastroenterology', 'Gastroenterology'),
                                        ('Geriatrics', 'Geriatrics'),
                                        ('Hematology', 'Hematology'),
                                        ('Cardiology', 'Cardiology'),
                                        ('Cancer_Medicine', 'Cancer_Medicine'),
                                        ('Clinical_Psychology', 'Clinical_Psychology'),
                                        ('Nephrology', 'Nephrology'),
                                        ('Neurophysiopathology', 'Neurophysiopathology'),
                                        ('Neurology', 'Neurology'),
                                        ('Paediatrics', 'Paediatrics'),
                                        ('Pediatric_Psychiatry', 'Pediatric_Psychiatry'),
                                        ('Sports_Medicine', 'Sports_Medicine'),
                                        ('Tropical_Medicine', 'Tropical_Medicine')))


doctor_obj = forms.ModelChoiceField(queryset=Doctor.objects.all())