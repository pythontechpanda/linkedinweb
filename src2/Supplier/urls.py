from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='homepage'),
    path('profile/',views.getProfileData, name="profile"),
    path('profile-edit/', views.EditProfile),
    path('company-details/', views.AboutCompany),
    path('com-details/', views.CompanyDetail),
    path('com-details-edit/<int:id>/', views.CompanyProfileEdit, name="detail"),
    path('new-post/', views.PostCreate, name="post_details"),
    path('like/', views.LikeView, name="like_post")
    
]
