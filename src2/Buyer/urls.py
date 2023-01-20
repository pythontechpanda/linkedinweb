from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='post_details'),    
    path('profile_detail/', views.profile_details, name='form'),
    path('profile/',views.getProfileData, name="profile"),
    path('like/', views.LikeView, name="like_post")
]
