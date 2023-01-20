from MyAdmin.models import Profile
from django.shortcuts import redirect, render
from accounts.models import User
from django.contrib import messages
from .models import *
from Supplier.models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
import geocoder
import folium
from geopy.geocoders import Nominatim

def demo(request):
    user_type = "Buyer"
    
    g=geocoder.ip("me")
    myadd=g.latlng
    print(myadd)
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(str(myadd[0])+","+str(myadd[1]))
    address = location.raw['address']
    # print(address)
    # print('City:',address['city'])
    # print('Country:',address['country'])
    return render(request, "buyer/index.html", {'user_type': user_type, 'address':address})


def profile_details(request):    
    if request.method == 'POST':
        address = request.POST['address']
        buying = request.POST['buy']
        looking = request.POST['looking']
        country = request.POST['country']
        state = request.POST['state']
        
        details = User.objects.filter(id=request.user.id)
        print(details)
        details.update(address=address, buying_op=buying, looking_for=looking, country=country, state=state)
        # details.save()
        messages.success(request, "Your Profile completed Enjoy MarketPlace Application.")
        return redirect('/buyer-app/')
    else:
        buy_op = BuyingOption.objects.all()
        look_for = LookingFor.objects.all()
        coun = Country.objects.all()
        sts = State.objects.all()
        user = User.objects.get(id=request.user.id)
        print(details)
              
        return render(request, "buyer/profile_complete.html", {'A':buy_op, 'B':look_for, 'C':coun, 'D':sts, 'user':user})




def getProfileData(request):
    g=geocoder.ip("me")
    myadd=g.latlng
    print(myadd)
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(str(myadd[0])+","+str(myadd[1]))
    address = location.raw['address']
    print(address)
    print('State:',address['state'])
    print('Country:',address['country'])
    # get user data
    data = User.objects.get(id=request.user.id)
    if data.is_staff:
        return render(request, "buyer/profile.html", {'data':data, 'address':address})
    else:
        data.is_staff=True
        print('----------------------------',data.is_staff)
        return render(request, "buyer/profile.html", {'data':data, 'address':address})





# def send_mail_after_registration(email , token):
#     subject = 'Your accounts need to be verified'
#     message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     send_mail(subject, message , email_from ,recipient_list )
    
