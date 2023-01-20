from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='homepage'),
    path('country/', views.add_country, name='country'),
    path('state/', views.add_state, name='state'),
    path('city/', views.add_city, name='city'),
    path('user/', views.User_list, name='user'),
    path('material/', views.MaterialOption, name='material'),
    path('buying/', views.BuyOption, name='buying'),
    path('looking/', views.LookingOption, name='looking'),
    
]
