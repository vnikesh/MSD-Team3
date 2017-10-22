from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def home(request):
    return render(request, 'eBedTrack/home.html',
                  {'eBedTrack': home})


def bed_availability(request):
    bed = Bed.objects.filter(created_date__lte=timezone.now())
    return render(request, 'eBedTrack/bed_availability.html',
                  {'beds': bed})


def eBedTrack_administrator(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)


def contact_us(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)


def hospital_list(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)


def nurse_list(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)


def patient_list(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)


def press_report(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)

