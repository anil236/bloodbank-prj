from dataclasses import fields
from pyexpat import model
from django import forms
from . models import donater ,requestclass

class donar_Registration(forms.ModelForm):
    class Meta:
        model =donater
        fields=['first_name','last_name','birthyear','email','ph_no','address','bloodgroup']
        
class request_Registration(forms.ModelForm):
    class Meta:
        model =requestclass
        fields=['user_name','birthyear','email','ph_no','address','bloodgroup']
        
