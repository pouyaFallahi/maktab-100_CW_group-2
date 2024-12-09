from django.shortcuts import render, redirect
from .models import Doctor, Patient
from django.views.generic.list import ListView
from django.http import HttpResponse
from .forms import DoctorModelForm, PatientForm, LoginForm
from django.contrib.auth import login, authenticate


def doctor_create(request):
    if request.method == 'POST':
        form = DoctorModelForm(request.POST)
        if form.is_valid():
            doctor_obj = Doctor()

    else:
        form = DoctorModelForm()
        context = {
            'form': form
        }
    return render(request, 'hospital/doctor_create.html', context)


def patient_create(request):
    form = PatientForm()
    context = {
        'form': form,
    }
    return render(request, 'patient_create.html', context)


def add_user(request):
    pass


def home(request):
    if request.COOKIES.get('visited'):
        response = HttpResponse('<h1 style="color: red">Welcome Back :)</h1>')
    else:
        response = HttpResponse('<h1>Welcome to Hospital Website</h1>')
        response.set_cookie('visited', True)
    return response



class PatientListView(ListView):
    model = Patient
    template_name = 'hospital/patient_listView.html'


class DoctorListView(ListView):
    model = Doctor

def log_in(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {'form': form}
        return render(request, 'hospital/login_page.html', context)

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('hospital:patient_list')
        return render(request, 'hospital/login_page', {'form': form})

