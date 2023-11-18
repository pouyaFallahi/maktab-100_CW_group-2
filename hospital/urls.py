from django.contrib import admin

from django.urls import path
from .views import doctor_list, patient_list, home

app_name = 'hospital'
urlpatterns = [
    path('main/', home, name='home'),
    path("doctor/", doctor_list, name='doctor'),
    path('patient/', patient_list, name='patient')
]
