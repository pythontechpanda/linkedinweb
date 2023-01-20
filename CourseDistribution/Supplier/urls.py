from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='homepage'),
    path('profile/',views.getProfileData, name="profile"),
    path('searchbuyer/',views.search_buyer, name="search")

]
