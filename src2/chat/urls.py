from django.urls import path

from . import views


urlpatterns = [
    path("chat/", views.index, name="index"),
    path("message/", views.chathome, name=""),
    path("<str:room_name>/", views.room, name="room"),
    
]