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
    return render(hospital_name, 'eBedTrack/bed_availability.html',
                  {'beds': bed})


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

    hospital = get_object_or_404()
    return render(request, 'eBedTrack/hospital_list.html',
                  {'hospitals': hospital})



def patient_list(request):

    patient = get_object_or_404()
    return render(request, 'eBedTrack/patient_list.html',
                  {'patients': patient})


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
            nurses = Nurse.objects.filter()
            return render(request, 'eBedTrack/nurse_list.html',
                {'nurses': nurses})

    else:
        form = NurseForm()
       # print("Else")
        return render(request, 'eBedTrack/nurse_list.html',
                      {'form': form})