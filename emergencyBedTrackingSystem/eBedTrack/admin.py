from django.contrib import admin
from .models import Patient, Nurse, Hospital, Administrator, Bed
# Register your models here.


class PatientList(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'sex', 'time_of_admission', 'condition', 'bed_type')
    list_filter = ('ph','first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    ordering = ['first_name', 'last_name']


class HospitalList(admin.ModelAdmin):
    list_display = ('hospital_id','hospital_name', 'address', 'phone_no')
    list_filter = ('hospital_name', 'phone_no')
    search_fields = ('hospital_name', 'address')
    ordering = ['hospital_name']


class NurseList(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')
    search_fields = ('nurse_id', 'first_name', 'last_name')
    ordering = ['first_name', 'last_name']


class BedList(admin.ModelAdmin):
    list_display = ('bed_id', 'bed_type', 'bed_count')
    list_filter = ('bed_id', 'bed_type','bed_count','bh')
    search_fields = ('bed_id', 'bed_type','bed_count')
    ordering = ['bed_id']


class AdminList(admin.ModelAdmin):
    list_display = ('admin_id', 'admin_name')
    list_filter = ('admin_id', 'admin_name')
    search_fields = ('admin_id', 'admin_name')
    ordering = ['admin_id']


admin.site.register(Patient, PatientList)
admin.site.register(Nurse, NurseList)
admin.site.register(Hospital, HospitalList)
admin.site.register(Administrator)
admin.site.register(Bed, BedList)
