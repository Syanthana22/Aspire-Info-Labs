from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('Behealthy.urls')),
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('login.html',views.login),
    path('checkup.html',views.checkup),
    path('fitness.html',views.fitness),
    path('awareness.html',views.awareness),
    path('emergency.html',views.emergency),
    path('score.html',views.score),
    path('home/user_medical_profile',views.user_medical_profile),
    path('home/emergency',views.emergency),
    path('home/awareness',views.awareness),
    path("home/checkup",views.checkup),
    path('chat/', views.chat, name='chat'),
    path("consult",views.consult),
    path("home/consult",views.consult),
]