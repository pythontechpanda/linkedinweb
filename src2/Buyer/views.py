from MyAdmin.models import Profile
from django.shortcuts import redirect, render, get_object_or_404
from accounts.models import User
from django.contrib import messages
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from Supplier.models import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
import geocoder
import folium
from geopy.geocoders import Nominatim

def demo(request):
    posts = CreatePost.objects.all().order_by("id").reverse()
  

    
    
    g=geocoder.ip("me")
    myadd=g.latlng
    print(myadd)
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(str(myadd[0])+","+str(myadd[1]))
    address = location.raw['address']
    # print(address)
    # print('City:',address['city'])
    print('Country:',address['country'])
    return render(request, "buyer/index.html", {'posts': posts, 'address':address})


def profile_details(request):    
    if request.method == 'POST':
        address = request.POST['address']
        buying = request.POST['buy']
        looking = request.POST['looking']
        country = request.POST['country']
        state = request.POST['state']
        
        details = User.objects.filter(id=request.user.id)
        details.update(address=address, buying_op=buying, looking_for=looking, country=country, state=state)
        # details.save()
        messages.success(request, "Your Profile completed Enjoy MarketPlace Application.")
        return redirect('/buyer-app/')
    else:
        buy_op = Qualification.objects.all()
        look_for = LookingFor.objects.all()
        coun = Country.objects.all()
        sts = State.objects.all()
        user = User.objects.get(id=request.user.id)
              
        return render(request, "buyer/profile_complete.html", {'A':buy_op, 'B':look_for, 'C':coun, 'D':sts, 'user':user})




def getProfileData(request):
    g=geocoder.ip("me")
    myadd=g.latlng
    print(myadd)
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(str(myadd[0])+","+str(myadd[1]))
    address = location.raw['address']
    # print(address)
    # print('City:',address['city'])
    print('Country:',address['country'])
    # get user data
    data = User.objects.get(id=request.user.id)
    return render(request, "buyer/profile.html", {'data':data, 'address':address})


def LikeView(request):
    user = request.user
    if request.method =="POST":
        post_id = request.POST.get('post_id')
        post_obj = CreatePost.objects.get(id=post_id)
        # profile = User.objects.get(user=request.user)
        
        
        if user in post_obj.like.all():
            post_obj.like.remove(user)
        else:
            post_obj.like.add(user)

        like, created = LikePost.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value='Like'

            post_obj.save()
            like.save()

    return redirect('/buyer-app/')

# def LikeView(request, id):
#     post = get_object_or_404(CreatePost, id=request.POST.get('post_id'))
#     post.like.add(request.user)
#     return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found')) 

# def send_mail_after_registration(email , token):
#     subject = 'Your accounts need to be verified'
#     message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     send_mail(subject, message , email_from ,recipient_list )
    
