from django import forms
from .models import Hospital, Bed, Patient, Nurse, ContactUs


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ('hospital_name', 'address', 'phone_no',)


class BedForm(forms.ModelForm):
    class Meta:
        model = Bed
        fields = (
            'bed_id','bed_type',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('firstName', 'lastName', 'emailId', 'question',)


class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ('nurse_id','first_name', 'last_name', 'address', 'phone_no', 'created_date',)


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'sex', 'time_of_admission', 'condition', 'mode_of_arrival', 'bed_type',)


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('age', 'birth_date', 'phone', 'injuries', 'deposition', 'time_of_surgery',
                  'kin_name', 'relation', 'time_of_death', 'phone',)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)