from django.db import models

# Create your models here.
class User_medical_profile(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)
    dob=models.DateField(max_length=8)
    contactNumber=models.CharField(max_length=13)
    email=models.EmailField(max_length=100)
    streetAddress=models.TextField()
    weight=models.IntegerField()
    height=models.IntegerField()
    allergies=models.TextField()
    medicalConditions=models.TextField()
    medications=models.TextField()
    surgeries=models.TextField()
    familyHistory=models.TextField()
    checkup=models.DateField()
    emergencyContactName=models.TextField()
    emergencyRelationship=models.TextField()
    emergencyContactNumber=models.CharField(max_length=13)
    class Meta:
        db_table='User_medical_profile'
class User_details(models.Model):
    username=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    year=models.IntegerField()
    section=models.IntegerField()
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    class Meta:
        db_table='User_details'
class Login_details(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    class Meta:
        db_table='Login_details'


class ChatMessage(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

