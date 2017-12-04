from django.utils import timezone
from django import template
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.forms import forms
from .forms import *
from .forms import LoginForm
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login

register = template.Library()


def home(request):
    return render(request, 'eBedTrack/home.html',
                  {'eBedTrack': home})

@login_required
def nurse_home(request):
    print('inside nurse home')
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
    h = Hospital.objects.all()
    dict = {}
    for x in h:
        e = Bed.objects.filter(bh_id=x).count()
        hos = Hospital.objects.get(hospital_id=str(x))
        dict[hos.hospital_name] = e
        print(dict)
    return render(request, 'eBedTrack/bed_availability.html',
                  {'hospitals': dict})


def bed_count(request):
    beds = Bed.objects.all()
    return render(request, 'eBedTrack/bed_availability.html',
                  {'beds': beds})


def eBedTrack_administrator(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)






def contact_us(request):
   if request.method == "POST":
       form = ContactForm(request.POST)
       if form.is_valid():
           contact = form.save(commit=False)
           contact.save()
           contacts = ContactUs.objects.filter(created_date=timezone.now())
           return render(request, 'eBedTrack/contact_us.html',
                         {'contacts': contacts})
   else:
       form = ContactForm()
       # print("Else")
   return render(request, 'eBedTrack/contact_us.html', {'form': form})





@login_required
def patient_list(request):
   print("inside patient list")
   print(request.user.username)
   print("inside patient list")
   pat = Patient.objects.filter(hospital_id=request.user.username)
   print(pat)
   return render(request, 'eBedTrack/patient_list.html', {'pat': pat})

# @login_required()
# def patient_new(request):
#     if request.method == "POST":
#         form = PatientForm(request.POST)
#         if form.is_valid():
#                 patient = form.save(commit=False)
#                 patient.created_date = timezone.now()
#                 print('displaying hospital_id '+ request.user.username)
#                 patient.save()
#                 pat = Patient.objects.filter(hospital_id=request.user.username)
#                 return render(request, 'eBedTrack/patient_list.html',
#                     {'pat': pat})
#     else:
#         form = PatientForm()
#         return render(request, 'eBedTrack/patient_new.html',
#                       {'form': form})

@login_required()
def patient_new(request):
    print('patient new')
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
                patient = form.save(commit=False)
                patient.created_date = timezone.now()
                hh = Hospital.objects.filter(hospital_id=request.user.username)[0]
                patient.hospital_id = hh
                patient.save()
                pat = Patient.objects.filter(hospital_id=request.user.username)
                print('printing pat '+str(pat))
                return render(request, 'eBedTrack/patient_list.html',
                    {'pat': pat})
        else :
            return render(request, 'eBedTrack/patient_new.html',
                          {'form': form})
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
            pat = Patient.objects.filter(hospital_id=request.user.username)
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
                hh = Hospital.objects.filter(hospital_id=request.user.username)[0]
                print('printing hh value '+str(hh))
                bed.bh=hh
                bed.save()

                e=request.user.username
                print('printing hh value '+str(hh))
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



def press_report(request):
    h = Hospital.objects.all()
    p = Patient.objects.all()
    pdict = {}
    dict = {}
    for x in h:
        e = Hospital.objects.get(hospital_name=x.hospital_name)
        dict[e.hospital_name] = e
        print("print e" , e)
        print(x)
        print(dict)
        for y in p:
            pc = Patient.objects.filter(hospital_id=x).count()
            con = Patient.objects.get(patient_tag=str(y))
            pdict[con.condition] = pc
            print(y)


    return render(request, 'eBedTrack/press_report.html',
                  {'press': pdict, 'hospitals':dict })






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






def success(request):
    return render(request, 'eBedTrack/success.html',
                  {'success': success})


def thanks(request):
    return render(request, 'eBedTrack/thanks.html',
                  {'thank': thanks})


def view_details(request):
    return render(request, 'eBedTrack/view_details.html',
                  {'view_details': view_details})


def privacy_statement(request):
    return render(request, 'eBedTrack/privacy_statement.html',
                  {'privacy_statement': privacy_statement})


def legal_notice(request):
    return render(request, 'eBedTrack/legal_notice.html',
                  {'legal_notice': legal_notice})

# @login_required
def admin_hospital_new(request):
   if request.method == "POST":
       form = HospitalForm(request.POST)
       if form.is_valid():
           hospital = form.save(commit=False)
           hospital.created_date = timezone.now()
           hospital.save()
           hospitals = HospitalForm.objects.filter(created_date__lte = timezone.now())
           return render(request, 'eBedTrack/admin_hospital_list.html',
                         {'hospitals': hospitals})
   else:
       form = HospitalForm()
       # print("Else")
   return render(request, 'eBedTrack/admin_hospital_new.html', {'form': form})



# @permission_required('entity.can_delete', login_url='/loginpage/')
def admin_home(request):

    return render(request, 'eBedTrack/admin_home.html',
                  {'eBedTrack': admin_home})

# @login_required
def nurse_new(request):
    nurseDetail = Nurse.objects.all()
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
        return render(request, 'eBedTrack/nurse_new.html',
                      {'form': form})



# @login_requireded
def nurse_list(request):
    nurses = Nurse.objects.all()
    print(nurses)
    return render(request, 'eBedTrack/nurse_list.html', {'nurses': nurses})



def admin_login(request):
    return render(request, 'eBedTrack/admin_login.html', {'eBedTrack': admin_login})
     # return HttpResponseRedirect('admin_login')

# @login_required
def admin_hospital_list(request):
    hospitals = Hospital.objects.filter(created_date__lte=timezone.now())
    return render(request, 'eBedTrack/admin_hospital_list.html',
                  {'hospitals': hospitals})

# @login_required
def admin_hospital_delete(request, pk):
   hospital = Hospital.objects.get(pk = pk)
   hospital.delete()
   hospitals = Hospital.objects.all()
   return render(request, 'eBedTrack/admin_hospital_list.html', {'hospitals': hospitals})

# @login_required
def admin_hospital_edit(request, pk):
   hospital = get_object_or_404(Hospital, pk  = pk)
   if request.method == "POST":
       form = HospitalForm(request.POST, instance=hospital)
       if form.is_valid():
           hospital = form.save()
           hospital.created_date = timezone.now()
           hospital.save()
           hospitals = Hospital.objects.filter(created_date__lte=timezone.now())
           return render(request, 'eBedTrack/admin_hospital_list.html', {'hospitals': hospitals})
   else:
       # print("else")
       form = HospitalForm(instance = hospital)
   return render(request, 'eBedTrack/admin_hospital_edit.html', {'form': form})

# @login_required
def nurse_delete(request, pk):
   nurse = Nurse.objects.get(pk = pk)
   nurse.delete()
   nurses = Nurse.objects.all()
   return render(request, 'eBedTrack/nurse_list.html', {'nurses': nurses})

# @login_required
def nurse_edit(request, pk):
   nurse = get_object_or_404(Nurse, pk  = pk)
   if request.method == "POST":
       form = NurseForm(request.POST, instance=nurse)
       if form.is_valid():
           nurse = form.save()
           nurse.created_date = timezone.now()
           nurse.save()
           nurses = Nurse.objects.filter(created_date__lte=timezone.now())
           return render(request, 'eBedTrack/nurse_list.html', {'nurses': nurses})
   else:
       # print("else")
       form = NurseForm(instance = nurse)
   return render(request, 'eBedTrack/nurse_edit.html', {'form': form})
