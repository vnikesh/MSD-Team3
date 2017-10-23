from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Patient(models.Model):
    patient_id = models.IntegerField(null=False, primary_key=True,default=6001)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    sex = models.CharField(max_length=10, null=False)
    time_of_admission = models.DateTimeField(default=timezone.now)
    condition = models.CharField(max_length=30)
    bed_type = models.CharField(max_length=10)
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

'''
    def save(self, *args, **kwargs):
        # On save, update timestamps
        if not self.id:
            self.created_date = timezone.now()
        self.update_date = timezone.now()
        return Pateint(User, self).save(*args, **kwargs)
'''


class Nurse(models.Model):
    nurse_id = models.AutoField(null=False, default=5001, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone_no = models.CharField(max_length=12)
    hospital_id = models.ForeignKey('Hospital' ,on_delete=models.CASCADE, related_name='hosnurses')
    admin_id = models.ForeignKey('Administrator', on_delete=models.CASCADE, related_name='admnurses')

    def __str__(self):
        return str(self.nurse_id)


class Bed(models.Model):
    bed_id = models.IntegerField(blank=False, null=False, primary_key=True,default=501)
    bed_type = models.CharField(max_length=50)
    hospital_id = models.ForeignKey('Hospital', on_delete=models.CASCADE, related_name='hosbeds')

    def __str__(self):
        return str(self.bed_id)


class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True,blank=False,default=1)
    hospital_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone_no = models.CharField(max_length=12)
    #admin_id = models.ForeignKey('Administrator',on_delete=models.CASCADE, related_name='hadmin')

    def __str__(self):
        return str(self.hospital_id)


class Administrator(models.Model):
    admin_id = models.AutoField(primary_key=True,default=101)
    admin_name = models.CharField(max_length= 100)


    def __str__(self):
        return str(self.admin_id)


'''
class Nurse_Bed(models.Model):
    nurse = models.ForeignKey('Nurse', on_delete=models.CASCADE, related_name='nurbeds')
    bed = models.ForeignKey('Bed_info', on_delete=models.CASCADE, related_name='bednurbeds')

    def __str__(self):
        return str(self.nurse)
'''



