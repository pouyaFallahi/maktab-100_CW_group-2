import phone_field
from django.db import models
from phone_field import PhoneField
from django.core.validators import MinValueValidator, MaxValueValidator


class UserModel(models.Model):
    gender_choices = (('MALE', 'male'), ('FEMALE', 'female'), ('OTHER', 'other'))
    first_name = models.CharField(max_length=250, null=False)
    last_name = models.CharField(max_length=250, null=False)
    gender = models.Choices(gender_choices)
    birth_date = models.DateField(DATE_INPUT_FORMATS=['%d-%m-%Y'], null=False)
    phone = PhoneField(null=False)
    email = models.EmailField()
    address = models.TextField(null=False)
    national_id = models.CharField(null=False)

    class Meta:
        abstract = True


class HealthInsurance(models.Model):
    company = models.CharField(null=False)
    address = models.TextField(null=False)
    phone = PhoneField(null=False)
    email = models.EmailField(blank=True)
    discount_percentage = models.FloatField(null=False)


class Patient(UserModel):
    patient_id = models.IntegerField(primary_key=True, serialize=True)
    health_insurance_id = models.ForeignKey(HealthInsurance, on_delete=models.CASCADE, related_name='patient',
                                            null=True)


class Doctor(UserModel):
    SPECIALTIES = [('Allergology&Immunology', 'Allergology&Immunology'),
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
                   ('Tropical_Medicine', 'Tropical_Medicine')]

    specialization = models.Choices(SPECIALTIES)
    medical_council_code = models.IntegerField(null=False)


class PatientHistory(models.Model):
    patient_id = models.OneToOneField(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField(DATETIME_FORMAT="%Y-%m-%d%H:%M:%S")
    diagnosis = models.TextField(null=False)
    prescription = models.TextField(null=False)
    drug_used = models.TextField(blank=True)
    note = models.TextField(blank=True)
    patient_history_id = models.IntegerField(primary_key=True, serialize=True)


class PatientBill(models.Model):
    patient_bill_id = models.IntegerField(serialize=True, primary_key=True)
    total_cost = models.FloatField(null=False)
    patient_history_id = models.ForeignKey(PatientHistory, on_delete=models.CASCADE)
    date = models.DateTimeField(DATETIME_FORMAT="%Y-%m-%d%H:%M:%S")
    insurance_contribution = models.FloatField(null=False)
    transaction_status = models.BooleanField(default=False)


class Appointment(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointment')
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointment')
    date = models.DateTimeField(DATETIME_FORMAT="%Y-%m-%d  %H:%M:%S")
    reason = models.TextField(null=False)
