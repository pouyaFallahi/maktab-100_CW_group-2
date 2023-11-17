from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import DoctorForm


def doctor_list(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():

            print(type(doctor_obj))


    else:
        form = DoctorForm()
        context = {
            'form': form
        }
    return render(request, 'hospital/doctor.html', context)


def patient_list(request):
    patient_list = Appointment.objects.all()
    pass


def add_user(request):
    pass
