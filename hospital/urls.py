from django.contrib import admin

from django.urls import path
from .views import doctor_create, patient_create, home, PatientListView

app_name = 'hospital'
urlpatterns = [
    path('main/', home, name='home'),
    path("doctor/", doctor_create, name='doctor'),
    path('patient-view/', PatientListView.as_view(), name='patient_list'),
    path('patient/', patient_create, name='patient')
]
