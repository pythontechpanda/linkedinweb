from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='homepage'),    
    path('profile_detail/', views.profile_details, name='form'),
    path('profile/',views.getProfileData, name="profile")
]
