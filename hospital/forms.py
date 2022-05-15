from dataclasses import field
from django import forms
from hospital.models import doctor,patient,booking,docupdate,contact

class DoctorReg(forms.ModelForm):
   class Meta:
      model=doctor
      fields="__all__"
      
class PatientReg(forms.ModelForm):
   class Meta:
      model=patient
      fields="__all__"
      
class Booking(forms.ModelForm):
    class Meta:
       model=booking
       fields="__all__"
       
class DocUpdate(forms.ModelForm):
    class Meta:
        model=docupdate
        fields="__all__"
class Contact(forms.ModelForm):
   class Meta:
      model=contact
      fields="__all__"  