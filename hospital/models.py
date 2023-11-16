import phone_field
from django.db import models
from phone_field import PhoneField


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
    pass


class Patient(UserModel):
    patient_id = models.IntegerField(primary_key=True, serialize=True)
    health_insurance_id = models.ForeignKey(HealthInsurance, on_delete=models.CASCADE, related_name='patient')


class Doctor(UserModel):
    specialization = models.CharField(null=False)
    medical_council_code = models.IntegerField(null=False)


class PatientHistory(models.Model):
    pass


class PatientBill(models.Model):
    pass


class Appointment(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointment')
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointment')
    date = models.DateTimeField(DATETIME_FORMAT="%Y-%m-%d  %H:%M:%S")
    reason = models.TextField(null=False)
