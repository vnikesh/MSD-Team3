from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.forms import forms
from .forms import *
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def home(request):
    return render(request, 'eBedTrack/home.html',
                  {'eBedTrack': home})

def nurse_home(request):
    return render(request, 'eBedTrack/nurse_home.html',
                  {'eBedTrack': nurse_home})

def nurse_bed_availability(request):
    print('inside hospital_list')
    e=request.user.username
    s=Bed.objects.filter(bh=e).values('bh', 'bed_type').annotate(Count('bed_type'))
    dict={}
    c=[]
    for j in s:
        c=[]
        for k,v in j.items():
            if k=='bh':
                continue
            else:
                c.append(v)
        dict[c[0]]=c[1]
    print (dict)
    hospitals = Hospital.objects.filter(created_date__lte=timezone.now())
    return render(request, 'eBedTrack/nurse_bed_availability.html',
                  {'s': dict})



def bed_availability(request):
    print('inside hospital_list')
    h = Hospital.objects.all()
    dict = {}
    for x in h:
        e = Bed.objects.filter(bh_id=x).count()
        hos = Hospital.objects.get(hospital_id=str(x))
        dict[hos.hospital_name] = e

    print(dict)

    return render(request, 'eBedTrack/bed_availability.html',
                  {'hospitals': dict})



#def bed_availability(request):
#    hospitals = Hospital.objects.all()
#    beds = Bed.objects.all()
#    return render(request, 'eBedTrack/bed_availability.html',
#                    {'hospitals': hospitals, 'beds': beds})


def bed_count(request):
    beds = Bed.objects.all()
    return render(request, 'eBedTrack/bed_availability.html',
                  {'beds': beds})


def eBedTrack_administrator(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)


# def contact_us(request):
#
#     form_class = forms
#
#     return render(request, 'eBedTrack/contact_us.html', {
#         'form': form_class,
#     })


def contact_us(request):
   if request.method == "POST":
       form = ContactForm(request.POST)
       if form.is_valid():
           contact = form.save(commit=False)
           contact.save()
           contacts = ContactUs.objects.filter(created_date=timezone.now())
           return render(request, 'eBedTrack/contact_us.html',
                         {'stocks': contacts})
   else:
       form = ContactForm()
       # print("Else")
   return render(request, 'eBedTrack/contact_us.html', {'form': form})



def hospital_list(request):

    hospitals = Hospital.objects.filter(created_date__lte=timezone.now())
    return render(request, 'eBedTrack/hospital_list.html',
                  {'hospitals': hospitals})

@login_required
def patient_list(request):
   print(request.user.username)
   print("inside patient list")
   pat = Patient.objects.filter(ph=request.user.username)
   print(pat)
   return render(request, 'eBedTrack/patient_list.html', {'pat': pat})

@login_required()
def patient_new(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
                patient = form.save(commit=False)
                patient.created_date = timezone.now()
                patient.save()
                pat = Patient.objects.filter(ph=request.user.username)
                return render(request, 'eBedTrack/patient_list.html',
                    {'pat': pat})
    else:
        form = PatientForm()
        return render(request, 'eBedTrack/patient_new.html',
                      {'form': form})


@login_required()
def personal(request):
    if request.method == "POST":
        form = PersonalForm(request.POST)
        if form.is_valid():
            personal = form.save(commit=False)
            personal.created_date = timezone.now()
            personal.save()
            pat = Patient.objects.filter(ph=request.user.username)
            return render(request, 'eBedTrack/patient_list.html',
                          {'pat': pat})

    else:
        form = PersonalForm()
        # print("Else")
        return render(request, 'eBedTrack/personal.html',
                      {'form': form})

@login_required()
def new_bed(request):
    print('inside nurse bed')
    if request.method == "POST":
        form = BedForm(request.POST)
        if form.is_valid():
                bed = form.save(commit=False)
                bed.created_date = timezone.now()
                bed.bh = 'UNMC'
                bed.save()

                e=request.user.username
                s=Bed.objects.filter(bh=e).values('bh', 'bed_type').annotate(Count('bed_type'))
                dict={}
                c=[]
                for j in s:
                    c=[]
                    for k,v in j.items():
                        if k=='bh':
                            continue
                        else:
                            c.append(v)
                    dict[c[0]]=c[1]

        return render(request, 'eBedTrack/nurse_bed_availability.html',
                    {'s': dict})
    else:
        form = BedForm()
        return render(request, 'eBedTrack/new_bed.html',
                      {'form': form})

"""

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


sex = [('male', 'female', 'others')]


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
"""

def press_report(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)
"""

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
"""



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
            return render(request, 'eBedTrack/bedcount_update.html',
                {'beds': beds})

    else:
        form = BedForm()
       # print("Else")
        return render(request, 'eBedTrack/bedcount_update.html',
                      {'form': form})


def nurse_login(request):
    return render(request, 'eBedTrack/nurse_login.html',
                  {'nurse': nurse_login})


def admin_login(request):
    return render(request, 'eBedTrack/user_login.html',
                  {'admin_login': admin_login})


def success(request):
    return render(request, 'eBedTrack/success.html',
                  {'success': success})


def thanks(request):
    return render(request, 'eBedTrack/thanks.html',
                  {'thank': thanks})


def press_report(request):
    print('inside hospital_list')
    h = Hospital.objects.all()
    dict = {}
    for x in h:
        e = Bed.objects.filter(bh_id=x).count()
        hos = Hospital.objects.get(hospital_id=str(x))
        dict[hos.hospital_name] = e

    print(dict)

    return render(request, 'eBedTrack/press_report.html',
                  {'hospitals': dict})

    hospitals = Hospital.objects.filter(created_date__lte=timezone.now())
    return render(request, 'eBedTrack/press_report.html',
                  {'hospitals': hospitals})


def user_login(request):
    print('inside admin_login')
    print('request method'+request.method)
    if request.method == 'POST':
        print('request method'+request.method)
        form = LoginForm(request.POST)
        if form.is_valid():
            print('form is valid')
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    return HttpResponse('Authenticated Successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        else:
            form = LoginForm()
        return render(request, 'account/login.html', {'form': form})
