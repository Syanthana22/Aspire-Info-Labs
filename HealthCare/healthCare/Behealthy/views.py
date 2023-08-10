from django.shortcuts import render
from Behealthy.models import User_details
from Behealthy.models import Login_details
from Behealthy.models import User_medical_profile
from Behealthy.forms import signupform
from Behealthy.forms import MedicalForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"
# Create your views here.
def fitness(request):
    return render(request,"fitness.html")
def Behealthy(request):
    return HttpResponse("Hello world!")
def home(request):
    return render(request,"home.html")
def awareness(request):
    return render(request,"awareness.html")
def emergency(request):
    return render(request,"emergency.html")
def checkup(request):
    return render(request,"checkup.html")
def signup(request):
    username=''
    email=''
    password1=''
    password2=''
    signup_form=signupform()
    if request.method == "POST":
        u=request.POST.get('username')
        e=request.POST.get('email')
        pwd=request.POST.get('password1')
        cpwd=request.POST.get('password2')
        signup_form=Login_details(username=u,email=e,password=pwd,confirm_password=cpwd)
        signup_form.save()
        return render(request,'home.html')
    else:
        return render(request,'userlogin.html')
def signin(request):
    username=''
    password1=''
   
    if request.method=="POST":
        u=request.POST.get('username')
        pwd1=request.POST.get('password1')
        m=sql.connect(host="localhost",user="root",password="system",database='Hackathon')
        
        cursor=m.cursor()
        d=request.POST
        c="select distinct * from Login_details"
        cursor.execute(c)
        t=cursor.fetchall()
        print(t)
        
        for i in t:
            if(u==i[1] and pwd1==i[4] ):
                return render(request,'home.html')
        else:
            return render(request,'home')
    return render(request,'userlogin.html')
        


'''
def signup(request):
    un=''
    nm='' 
    dept=''
    year=0 
    sec=0
    password1=''
    password2=''
    signup_form=signupform()
    if request.method == "POST":
        u=request.POST.get('un')
        n=request.POST.get('nm')
        d=request.POST.get('dept')
        y=request.POST.get('year')
        s=request.POST.get('sec')
        pwd=request.POST.get('password1')
        cpwd=request.POST.get('password2')
        signup_form=User_details(username=u,name=n,department=d,year=y,section=s,password=pwd,confirm_password=cpwd)
        signup_form.save()
        return render(request,'welcome.html')
    else:
        
        return render(request,'signup.html')
'''
def user_medical_profile(request):
    firstname=''
    lastname=''
    gender=''
    dob=''
    contact=''
    email=''
    street=''
    weight=''
    height=''
    allergies=''
    medicalConditions=''
    medications=''
    surgeries=''
    familyHistory=''
    checkup=''
    emergencyContactName=''
    emergencyRelationship=''
    emergencyContactNumber=''
    
    medical_form=MedicalForm()
    if request.method=="POST":
        fn=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        contact=request.POST.get('contactNumber')
        email=request.POST.get('email')
        street=request.POST.get('streetAddress')
        weight=request.POST.get('weight')
        height=request.POST.get('height')
        allergies=request.POST.get('allergies')
        medicalConditions=request.POST.get('medicalConditions')
        medications=request.POST.get('medications')
        surgeries=request.POST.get('surgeries')
        familyHistory=request.POST.get('familyHistory')
        checkup=request.POST.get('checkup')
        emergencyContactName=request.POST.get('emergencyContactName')
        emergencyRelationship=request.POST.get('emergencyRelationship')
        emergencyContactNumber=request.POST.get('emergencyContactNumber')
        print(fn)
        medical_form=User_medical_profile(firstname=fn,lastname=lastname,gender=gender,dob=dob,contactNumber=contact,email=email,streetAddress=street,weight=weight,height=height,allergies=allergies,medicalConditions=medicalConditions,medications=medications,surgeries=surgeries,familyHistory=familyHistory,checkup=checkup,emergencyContactName=emergencyContactName,emergencyRelationship=emergencyRelationship,emergencyContactNumber=emergencyContactNumber)
        medical_form.save()
        return render(request,'welcome.html')
    else:
        return render(request,'user_medical_profile')


# chatbot/views.py
from django.shortcuts import render
from .openai_api import generate_response

def chat(request):
    context = {}
    if request.method == 'POST':
        user_input = request.POST['user_input']
        bot_response = generate_response(user_input)
        context['user_input'] = user_input
        context['bot_response'] = bot_response
    return render(request, 'chat.html', context)
def score(request):
    return render(request,"score.html")
def consult(request):
    return render(request,"consult.html")        







