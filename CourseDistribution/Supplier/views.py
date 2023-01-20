from django.shortcuts import render
from accounts.models import User
import geocoder
import folium
from geopy.geocoders import Nominatim

def demo(request):
    user_type = "Supplier"
    return render(request, "supplier/index.html", {'user_type':user_type})

def search_buyer(request):
    if request.method=='POST':
        searched=request.method['searched']
        buyer=User.objects.filter(name__contain=searched,is_staff=True)
        return render(request,"supplier/profile.html",{'buyer':buyer})
    else:
        return render(request,"supplier/profile.html")


def getProfileData(request):
    g=geocoder.ip("me")
    myadd=g.latlng
    print(myadd)
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(str(myadd[0])+","+str(myadd[1]))
    address = location.raw['address']
    # print(address)
    print('State:',address['state'])
    print('Country:',address['country'])
    
    #get user data
    data = User.objects.get(id=request.user.id)
    return render(request, "supplier/profile.html", {'data':data, 'address':address})
