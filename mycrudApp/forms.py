from django import forms
from django.core.exceptions import ValidationError
from .models import *

class stu_reg_frm(forms.ModelForm):
    
    class Meta:
        model = stu_info
        fields = ['stu_name', 'mobile_no', 'age'] 
        labels = {
            'stu_name': 'Full Name',
            'mobile_no': 'Mobile No',
            'age': 'Age Of Student',
        }
        widgets ={
            'stu_name':forms.TextInput(attrs={'class':'form-control', 'id':'stu_name','autofocus':'autofocus'}),
            'mobile_no':forms.NumberInput(attrs={'class':'form-control', 'id':'mobile_no'}),
            'age':forms.NumberInput(attrs={'class':'form-control', 'id':'age'})
        }
        error_messages ={
            'stu_name':{'required':'Name Field Can not be blank'},
            'mobile_no':{'required':'Mobile Field Can not be blank'},
            'age':{'required':'Age Field Can not be blank'}
        }   

    def clean_stu_name(self , *args, **kwargs):
        stu_name = self.cleaned_data.get("stu_name")
        if stu_name.isalpha():
            return stu_name
        else:
            raise forms.ValidationError('Name Must be Alphabet')
    def clean_mobile_no(self, *args, **kwargs):
        mobile_no =  self.cleaned_data.get('mobile_no')
        if len(str(mobile_no)) != 10:
            raise ValidationError("Mobile No must be 10 digits")            
        else:
            return mobile_no
    def clean_age(self, *args, **kargs):
        age = self.cleaned_data.get('age')
        if age > 18 and age < 100:
            return age
        else:
            raise ValidationError("Age must be between 18 to 100")    
        
            
        