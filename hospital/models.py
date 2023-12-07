from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class UserModel(models.Model):
    gender_choices = [('MALE', 'male'), ('FEMALE', 'female'), ('OTHER', 'other')]
    first_name = models.CharField(max_length=250, null=False)
    last_name = models.CharField(max_length=250, null=False)
    gender = models.CharField(max_length=50, default='FEMALE', choices=gender_choices)
    birth_date = models.DateField()
    phone = models.CharField(max_length=14, null=False)
    email = models.EmailField()
    address = models.TextField(null=False)
    national_id = models.CharField(max_length=100, null=False)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    class Meta:
        abstract = True


class DaysModel(models.Model):
    DAYS_OF_WEEK = [
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('wednesday', 'wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday')
    ]
    days_of_attendance = models.CharField(choices=DAYS_OF_WEEK, max_length=10, null=True, blank=True)

    class Meta:
        abstract = True


class HealthInsurance(models.Model):
    company = models.CharField(max_length=100, null=False)
    address = models.TextField(null=False)
    phone = models.CharField(max_length=14, null=False)
    email = models.EmailField(blank=True)
    discount_percentage = models.FloatField(null=False)

    def __str__(self):
        return f'{self.company}'


class Patient(UserModel):
    patient_id = models.IntegerField(primary_key=True, serialize=True)
    health_insurance_id = models.ForeignKey(HealthInsurance, on_delete=models.CASCADE, related_name='patient',
                                            null=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Doctor(UserModel, DaysModel):
    doctor_id = models.IntegerField(primary_key=True, serialize=True)
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
    # DAYS_OF_WEEK = [
    #     ('Saturday', 'Saturday'),
    #     ('Sunday', 'Sunday'),
    #     ('Monday', 'Monday'),
    #     ('Tuesday', 'Tuesday'),
    #     ('wednesday', 'wednesday'),
    #     ('Thursday', 'Thursday'),
    #     ('Friday', 'Friday')
    # ]
    specialization = models.CharField(max_length=50, choices=SPECIALTIES, default='Allergology&Immunology')
    medical_council_code = models.IntegerField(null=False)

    # days_of_attendance = models.CharField(max_length=50, choices=DAYS_OF_WEEK)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class PatientHistory(models.Model):
    patient_id = models.OneToOneField(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    diagnosis = models.TextField(null=False)
    prescription = models.TextField(null=False)
    drug_used = models.TextField(blank=True)
    note = models.TextField(blank=True)
    patient_history_id = models.IntegerField(primary_key=True, serialize=True)


class PatientBill(models.Model):
    patient_bill_id = models.IntegerField(serialize=True, primary_key=True)
    total_cost = models.FloatField(null=False)
    patient_history_id = models.ForeignKey(PatientHistory, on_delete=models.CASCADE)
    date = models.DateTimeField()
    insurance_contribution = models.FloatField(null=False)
    transaction_status = models.BooleanField(default=False)


class Appointment(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointment')
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointment')
    date = models.DateTimeField()
    reason = models.TextField(null=False)
