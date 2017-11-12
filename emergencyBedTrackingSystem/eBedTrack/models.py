from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Patient(models.Model):
    patient_id = models.IntegerField(null=False, primary_key=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    #sex = models.CharField(max_length=10, null=False)
    MALE = 'M'
    FEMALE = 'F'
    type_of_sex = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    )
    sex = models.CharField(max_length=10,
                                      choices=type_of_sex,
                                      default=MALE)
    time_of_admission = models.DateTimeField(default=timezone.now)
    condition = models.CharField(max_length=30)
    ICU = '1'
    EU = '2'
    OTHER = '3'
    type_of_bed= (
        (ICU,'ICU'),
        (EU,'EU'),
        (OTHER,'OTHER'),
    )
    bed_type = models.CharField(max_length=10, choices=type_of_bed,default='ICU ')
    bed_id = models.CharField(max_length=20,default=0)
    mode_of_arrival = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=10)
    injuries = models.CharField(max_length=50,blank=True)
    deposition = models.CharField(max_length=50, blank=True)
    time_of_surgery = models.CharField(max_length=20,blank=True)
    kin_name = models.CharField(max_length=50,blank=True)
    relation = models.CharField(max_length=50,blank=True)
    time_of_death = models.CharField(max_length=20,blank=True)
    created_date = models.DateTimeField(default=timezone.now,blank=True)
    updated_date = models.DateTimeField(auto_now_add=True, null = True)
    nurse_id = models.ForeignKey("Nurse", on_delete=models.CASCADE, related_name='nurpatients', null=True)


    def created(self):
        self.time_of_admission = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.patient_id)


class Nurse(models.Model):
    nurse_id = models.AutoField(null=False, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone_no = models.CharField(max_length=12)
    created_date = models.DateField(default=timezone.now, blank=True, null=True)
    hospital_id = models.ForeignKey('Hospital',on_delete=models.CASCADE, related_name='hosnurses')
    admin_id = models.ForeignKey('Administrator', on_delete=models.CASCADE, related_name='admnurses')

    def __str__(self):
        return str(self.nurse_id)


class Bed(models.Model):
    bed_id = models.IntegerField(blank=False, null=False, primary_key=True)
    bed_type = models.CharField(max_length=50)
    bed_count = models.CharField(max_length=25)
    created_date = models.DateField(default=timezone.now)
    bh = models.ForeignKey('Hospital', on_delete=models.CASCADE, related_name='hosbeds')

    def __str__(self):
        self.save()
        return str(self.bed_id)




class Hospital(models.Model):
    hospital_id = models.IntegerField(null=False, primary_key=True)
    hospital_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone_no = models.CharField(max_length=12)
    created_date = models.DateField(default=timezone.now)
    #admin_id = models.ForeignKey('Administrator',on_delete=models.CASCADE, related_name='hadmin')

    def __str__(self):
        self.save()
        return str(self.hospital_id)

class Administrator(models.Model):
    admin_id = models.AutoField(null=False, primary_key=True)
    admin_name = models.CharField(max_length= 100)

    def __str__(self):
        self.save()
        return str(self.admin_id)

