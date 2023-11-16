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
    health_insurance_id = models.ForeignKey(HealthInsurance, on_delete=models.CASCADE, related_name='patient', null=True)


class Doctor(UserModel):
    specialization = models.CharField(null=False)
    medical_council_code = models.IntegerField(null=False)


class PatientHistory(models.Model):
    patient_id = models.OneToOneField(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField(DATETIME_FORMAT="%Y-%m-%d%H:%M:%S")
    diagnosis = models.TextField(null=False)
    prescription = models.TextField(null=False)
    drug_used = models.TextField(blank=True)
    note = models.TextField(blank=True)
    patient_history_id = models.IntegerField()


class PatientBill(models.Model):
    patient_bill_id = models
    patient_history_id = models.OneToOneField(PatientHistory, on_delete=models.CASCADE)


class Appointment(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointment')
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointment')
    date = models.DateTimeField(DATETIME_FORMAT="%Y-%m-%d  %H:%M:%S")
    reason = models.TextField(null=False)