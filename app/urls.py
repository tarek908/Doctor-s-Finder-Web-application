from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('appointment/', views.appointment, name='appointment'),
    path('team/', views.team, name='team'),
    path('feature/', views.feature, name='feature'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('404/', views.error, name='404'),
    path('RegForm/', views.RegForm, name='RegForm'),
    path('LogForm/', views.LogForm, name='LogForm'),

    #### -user Profile - ####
    path('userProfile/', views.userProfile, name='userProfile'),
    path('userSignup/', views.userSignup, name='userSignup'),
    path('userLogin/', views.userLogin, name='userLogin'),
    path('userSignin/', views.userSignin, name='userSignin'),
    path('login/', views.login, name='login'),

    #### - Deshbord - ####
    path('DrProfile/', views.DrProfile, name='DrProfile'),
    path('DrRegister/', views.DrRegister, name='DrRegister'),
    path('DrLogin/', views.DrLogin, name='DrLogin'),
    path('DrInfo/<int:pk>', views.DrInfo, name='DrInfo'),
    path('UpdateInfo/<int:pk>', views.UpdateInfo, name='UpdateInfo'),
    path('updateProfile/<int:pk>', views.updateProfile, name='updateProfile'),

    #### - Appointment - ####
    path('GetAppointment/', views.GetAppointment, name='GetAppointment'),

    #### - Appointment status - ####
    path('status/<int:pk>', views.status, name='status'),
    path('appStatus/<int:pk>', views.appStatus, name='appStatus'),
    
    #### - Rating -####
    path('ratingPage/', views.ratingPage, name='ratingPage'),
    path('getRating/', views.getRating, name='getRating'),

    #### - Patient logout - ####
    path('Patlogout', views.Patlogout, name='Patlogout'),
    path('Drlogout', views.Drlogout, name='Drlogout'),

    #### - Admin - ####
    path('adminIndex/', views.adminIndex, name='adminIndex'),
    path('adlogin/', views.AdminLogin, name='AdminLogin'),
    path('AdminSignin/', views.AdminSignin, name='AdminSignin'),
    path('drVerification/<int:pk>', views.drVerification, name='drVerification'),
    path('drVerifi/<int:pk>', views.drVerifi, name='drVerifi'),
    path('drDelete/<int:pk>', views.drDelete, name='drDelete'),
]
