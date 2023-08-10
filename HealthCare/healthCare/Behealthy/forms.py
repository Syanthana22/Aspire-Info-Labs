from django import forms
from Behealthy.models import User_details
from Behealthy.models import User_medical_profile
from Behealthy.models import Login_details
''' 
class signupform(forms.Form):
    username=forms.CharField(max_length=100)
    name=forms.CharField(max_length=100)
    department=forms.CharField(max_length=100)
    section=forms.IntegerField()
    year=forms.IntegerField()
    password=forms.CharField(max_length=100)
    confirm_password=forms.CharField(max_length=100)
class StudentForm(forms.ModelForm):
    class Meta:
        model=User_details
        fields=["username","name","department","section","year","password","confirm_password"]
'''
class MedicalForm(forms.Form):
    firstname=forms.CharField(max_length=100)
    lastname=forms.CharField(max_length=100)
    gender=forms.CharField(max_length=20)
    dob=forms.DateField()
    contactNumber=forms.IntegerField()
    email=forms.EmailField(max_length=100)
    streetAddress=forms.CharField(widget=forms.Textarea)
    weight=forms.IntegerField()
    height=forms.IntegerField()
    allergies=forms.CharField(widget=forms.Textarea)
    medicalConditions=forms.CharField(widget=forms.Textarea)
    medications=forms.CharField(widget=forms.Textarea)
    surgeries=forms.CharField(widget=forms.Textarea)
    familyHistory=forms.CharField(widget=forms.Textarea)
    checkup=forms.DateField()
    emergencyContactName=forms.CharField(widget=forms.Textarea)
    emergencyRelationship=forms.CharField(widget=forms.Textarea)
    emergencyContactNumber=forms.IntegerField()
class MedicalForm(forms.ModelForm):
    class Meta:
        model=User_medical_profile
        fields=["firstname","lastname","gender","dob","contactNumber","email","streetAddress","weight","height","allergies","medicalConditions","medications","surgeries","familyHistory","checkup","emergencyContactName","emergencyRelationship","emergencyContactNumber"]
class signupform(forms.Form):
    username=forms.CharField(max_length=100)
    email=forms.EmailField()
    password=forms.CharField(max_length=100)
    confirm_password=forms.CharField(max_length=100)
class signupform(forms.ModelForm):
    class Meta:
        model=Login_details
        fields=["username","email","password","confirm_password"]
