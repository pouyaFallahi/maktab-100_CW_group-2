from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def doctor(request):
    doctor_obj = Doctor.objects.all()
    patient_list = Appointment.objects.all()
    return HttpResponse(';ldfgkj[weqfogiklnhj')


def add_patient(request):
    pass


def patient(request):
    pass
