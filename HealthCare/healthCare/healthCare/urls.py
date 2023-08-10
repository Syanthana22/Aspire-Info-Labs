"""healthCare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Behealthy import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("Behealthy/", views.Behealthy),
    path("",views.signup),
    path('home/',views.home),
    path('home.html',views.home),
    path('signin',views.signin),
    path('checkup',views.checkup),
    path('fitness',views.fitness),
    path('awareness',views.awareness),
    path('emergency',views.emergency),
    path("user_medical_profile/",views.user_medical_profile),
    path("signup/",views.signup),
    path("home/fitness",views.fitness),
    path("home/userlogin",views.signup),
    path("home/awareness",views.awareness),
    path("home/emergency",views.emergency),
    path("home/checkup",views.checkup),
    path("home/user_medical_profile",views.user_medical_profile),
    path("fitness#home",views.home),
    path("home/score",views.score),
    path("score",views.score),
    path("consult",views.consult),
    path("home/consult",views.consult),
    path('chat/', views.chat, name='chat'),
    
]
