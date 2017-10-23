from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.forms import forms
from .forms import *


def home(request):
    return render(request, 'eBedTrack/home.html',
                  {'eBedTrack': home})


def bed_availability(hospital_name):
    bed = get_object_or_404(Bed)
    hospitals = Hospital.objects.filter(created_date__lte=timezone.now())
    return render(hospital_name, 'eBedTrack/bed_availability.html',
                  {'beds': bed,
                   'hospitals': hospitals})


def eBedTrack_administrator(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)


def contact_us(request):

    form_class = forms

    return render(request, 'eBedTrack/contact_us.html', {
        'form': form_class,
    })


def hospital_list(request):

    hospitals = Hospital.objects.filter(created_date__lte=timezone.now())
    return render(request, 'eBedTrack/hospital_list.html',
                  {'hospitals': hospitals})


@login_required()
def patient_list(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
                patient = form.save(commit=False)
                patient.created_date = timezone.now()
                patient.save()
                patients = Patient.objects.filter(created_date__lte=timezone.now())
                return render(request, 'eBedTrack/patient_list.html',
                    {'patients': patients})

    else:
        form = PatientForm()
        return render(request, 'eBedTrack/patient_list.html',
                      {'form': form})

@login_required()
def personal(request):
    if request.method == "POST":
        form = PersonalForm(request.POST)
        if form.is_valid():
            personal = form.save(commit=False)
            personal.created_date = timezone.now()
            personal.save()
            personals = Patient.objects.filter(created_date__lte=timezone.now())
            return render(request, 'eBedTrack/patient_list.html',
                          {'personals': personals})

    else:
        form = PersonalForm()
        # print("Else")
        return render(request, 'eBedTrack/patient_list.html',
                      {'form': form})


def press_report(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)


@login_required
def nurse_list(request):
    if request.method == "POST":
        form = NurseForm(request.POST)
        if form.is_valid():
            nurse = form.save(commit=False)
            nurse.created_date = timezone.now()
            nurse.save()
            nurses = Nurse.objects.filter(created_date__lte=timezone.now())
            return render(request, 'eBedTrack/nurse_list.html',
                {'nurses': nurses})

    else:
        form = NurseForm()
       # print("Else")
        return render(request, 'eBedTrack/nurse_list.html',
                      {'form': form})


@login_required
def bedcount_update(request):
    if request.method == "POST":
        form = BedForm(request.POST)
        if form.is_valid():
            bed = form.save(commit=False)
            bed.created_date = timezone.now()
            bed.save()
            beds = Bed.objects.filter(created_date__lte=timezone.now())
            return render(request, 'eBedTrack/nurse_list.html',
                {'beds': beds})

    else:
        form = BedForm()
       # print("Else")
        return render(request, 'eBedTrack/bedcount_update.html',
                      {'form': form})