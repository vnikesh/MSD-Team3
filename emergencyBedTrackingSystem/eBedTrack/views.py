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
from django.db.models import Count


def home(request):
    return render(request, 'eBedTrack/home.html',
                  {'eBedTrack': home})


def adminlogin(request):

    if request.user.is_staff:
        return redirect('eBedTrack/nurse_login.html')
    else:
        return redirect('eBedTrack/admin_login.html')


@login_required()
def nurse_home(request):
    print('inside nurse home')
    user_name = request.user.username
    for hosp in Hospital.objects.raw('select hospital_id,hospital_name from eBedTrack_Hospital '
                                     'where hospital_id=%s',[user_name]):
        print('print hospital id ')
        print(hosp.hospital_id)
        print('The hospital name is ')
        print(hosp.hospital_name)
        name = hosp.hospital_name
    return render(request, 'eBedTrack/nurse_home.html',
                  {'hosp_name':name})


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
    print('inside first responder bed_availability')
    h = Hospital.objects.all()
    # print(h)
    # for hosp in h:
    #     print(hosp)
    dict = {}
    for x in h:
        e = Bed.objects.filter(bh_id=x).count()
        hos = Hospital.objects.get(hospital_id=str(x))
        dict[hos.hospital_name] = e
        s = Bed.objects.filter(bh=x, status='VACANT').values('bh', 'bed_type').annotate(Count('bed_type'))
        bedtype = {}
        print('printing bedtype for hospital ' + str(x))
        for j in s:
            c = []
            for k, v in j.items():
                if k == 'bh':
                    continue
                else:
                    c.append(v)
            bedtype[c[0]] = c[1]
            print(bedtype)
        h = Hospital.objects.all()
        hospitals = Hospital.objects.filter(created_date__lte=timezone.now())
    return render(request, 'eBedTrack/bed_availability.html',
                      {'hospitals': dict})


    # print('inside hospital_list')
    # h = Hospital.objects.all()
    # dict = {}
    # for x in h:
    #     e = Bed.objects.filter(bh_id=x).count()
    #     hos = Hospital.objects.get(hospital_id=str(x))
    #     dict[hos.hospital_name] = e
    #
    # return render(request, 'eBedTrack/bed_availability.html',
    #               {'hospitals': dict})



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
                         {'stocks': contacts})
   else:
       form = ContactForm()
       # print("Else")
   return render(request, 'eBedTrack/contact_us.html', {'form': form})



def hospital_list(request):
    hospitals = Hospital.objects.filter(created_date__lte=timezone.now())
    return render(request, 'eBedTrack/hospital_list.html',
                  {'hospitals': hospitals})


# def bed_availability(request):
#     print('inside hospital_list')
#     h = Hospital.objects.all()
#     print('hospital obj'+str(h))
#     dict = {}
#     for x in h:
#         e = Bed.objects.filter(bh_id=x).count()
#         hos = Hospital.objects.get(hospital_id=str(x))
#         dict[hos.hospital_name] = e
#         print(dict)
#     return render(request, 'eBedTrack/bed_availability.html',
#                   {'hospitals': dict})

@login_required()
def nurse_bed_availability(request):
    print('inside nurse bed availability')
    e=request.user.username
    #bedtype = Bed.objects.raw("select bed_id,bed_type,count(*) from eBedTrack_Bed where status='VACANT' group by bed_type")
    #print('query o/p' +str(bedtype))
    s=Bed.objects.filter(bh=e,status='VACANT').values('bh', 'bed_type').annotate(Count('bed_type'))
    bedtype={}
    for j in s:
        c=[]
        for k,v in j.items():
            if k=='bh':
                continue
            else:
                c.append(v)
        bedtype[c[0]]=c[1]
    print (bedtype)
    h = Hospital.objects.all()
    print('hospital obj'+str(h))
    hospitals = Hospital.objects.filter(created_date__lte=timezone.now())
    return render(request, 'eBedTrack/nurse_bed_availability.html',
                  {'s': bedtype})

@login_required
def patient_list(request):
   print("inside patient list")
   print(request.user.username)
   patient = Patient.objects.filter(hospital_id=request.user.username)
   # print('printing patients '+str(patient))
   return render(request, 'eBedTrack/patient_list.html', {'patients': patient})

@login_required()
def patient_new(request):
    print('inside patient new')
    un = request.user.username
    if request.method == "POST":
        form = PatientForm(request.POST)
        bid =form.data['bed_id']
        print('printing bedid from form '+ str(bid))
        pbid = str(un) + str(bid)
        print(form.data)

        mutable = request.POST._mutable
        print('mutable :'+ str(mutable))
        request.POST._mutable = True
        request.POST['bed_id'] = pbid
        request.POST._mutable = mutable

        if form.is_valid():
                print('form is valid')
                patient = form.save(commit=False)
                s = form.cleaned_data.get('patient_tag')
                print('printing from form - patient_tag '+ str(s))
                patient.created_date = timezone.now()
                hh = Hospital.objects.filter(hospital_id=request.user.username)[0]
                patient.hospital_id= hh
                patient.save()
                pat = Patient.objects.filter(hospital_id=request.user.username)
                print('printing pat '+str(pat))
                h = Hospital.objects.all()
                print('what is in h ' + str(h))
                hbed = form.cleaned_data.get('bed_id')
                print('printing from form - bed id ')
                print(hbed)
                q = Bed.objects.filter(bed_id=str(hbed)).update(status='OCCUPIED')
                print('updated ')
                return render(request, 'eBedTrack/patient_list.html',
                    {'patients': pat})
        else :
            return render(request, 'eBedTrack/patient_new.html',
                          {'form': form})
    else:
        form = PatientForm()
        return render(request, 'eBedTrack/patient_new.html',
                      {'form': form})

@login_required
def patient_edit(request, pk):
    print('inside patient_edit')
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.updated_date = timezone.now()
            patient.save()
            s = form.cleaned_data.get('patient_status')
            if s=='Discharged':
                Pat=Patient.objects.filter(id=pk).values('bed_id')
                for i in Pat:
                    for k,v in i.items():
                        Bed.objects.filter(bed_id=v).update(status='VACANT')

            patient = Patient.objects.filter(created_date__lte=timezone.now())
            return render(request, 'eBedTrack/patient_list.html',
                         {'patients': patient})
        else:
            form = PatientForm(instance=patient)
            return render(request, 'eBedTrack/patient_edit.html', {'form': form})

    else:
        form = PatientForm(instance=patient)
        return render(request, 'eBedTrack/patient_edit.html', {'form': form})


@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    Pat=Patient.objects.filter(id=pk).values('bed_id')
    print (Pat)
    for i in Pat:
        for k,v in i.items():
            Bed.objects.filter(bed_id=v).update(status='VACANT')

    print('Pat is '+str(Pat))
    patient.delete()

    return redirect('eBedTrack:patient_list')


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
    print('inside nurse new bed')
    uname = request.user.username
    print(uname)
    if request.method == "POST":
        print('form method is POST')
        form = BedForm(request.POST)
        bid =form.data['bed_id']
        print('printing bedid from form '+ str(bid))
        pbid = str(uname) + str(bid)
        print(form.data)

        mutable = request.POST._mutable
        print('mutable :'+ str(mutable))
        request.POST._mutable = True
        request.POST['bed_id'] = pbid
        request.POST._mutable = mutable

        if form.is_valid():
                print('yes, form is valid')
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
        print('form is invalid')
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

    # print(dict)
    # print(p)

    # dict1 = {}
    # for x in p:
    #     e1 = Patient.objects.filter(patient_id=x)
    #     hos1 = Patient.objects.get(patient_id=str(x))
    #     dict[hos1.condition] = e1


    return render(request, 'eBedTrack/press_report.html',
                  {'press': pdict, 'hospitals':dict })



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


def view_details(request):
    # return render(request, 'eBedTrack/view_details.html',
    #               {'view_details': view_details})

    print('inside hospital_list')
    hosp = Hospital.objects.all()
    be = Bed.objects.all()
    pdict = {}

    for x in hosp:
        e = Hospital.objects.filter(hospital_id=x)
        print(e)
        for y in be:
            f = Bed.objects.filter(bed_type=y).count()
            b = Bed.objects.get(bed_type=str(y))
            print(b)
            print(f)
            pdict[b.bed_type] = f
            print(pdict)
    return render(request, 'eBedTrack/view_details.html',
                {'pdict': pdict})


def privacy_statement(request):
    return render(request, 'eBedTrack/privacy_statement.html',
                  {'privacy_statement': privacy_statement})


def legal_notice(request):
    return render(request, 'eBedTrack/legal_notice.html',
                  {'legal_notice': legal_notice})

