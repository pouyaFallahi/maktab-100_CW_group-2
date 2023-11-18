from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import DoctorForm, PatientForm


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
    patient_list = Patient.objects.all()
    form = PatientForm()
    context = {
        'form': form,
        'patient_list': patient_list
    }
    return render(request, 'patient_list.html', context)


def add_user(request):
    pass


def home(request):
    if request.COOKIES.get('visited'):
        response = HttpResponse('<h1 style="color: red">Welcome Back :)</h1>')
    else:
        response = HttpResponse('<h1>Welcome to Hospital Website</h1>')
        response.set_cookie('visited', True)
    return response