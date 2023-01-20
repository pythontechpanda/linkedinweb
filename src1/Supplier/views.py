from django.shortcuts import render, redirect
from accounts.models import User
from Supplier.models import CoursesOptions, Country,State,City
from django.contrib import messages
from Supplier.models import *
import geocoder
import folium
from geopy.geocoders import Nominatim

def demo(request):
    user_type = "Supplier"
    return render(request, "supplier/index.html", {'user_type':user_type})



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
    
    #get user data
    data = User.objects.get(id=request.user.id)
    return render(request, "supplier/profile.html", {'data':data, 'address':address})


def EditProfile(request):
    prod = CoursesOptions.objects.all()
    country = Country.objects.all()
    state= State.objects.all()
    if request.method == "POST":
        name = request.POST['fname']
        email = request.POST['email']
        username = request.POST['username']
        # dp = request.FILES['profile_img']
        # bg_img = request.FILES['backgroud_img']
        state = request.POST['state']
        country = request.POST['country']
        contact = request.POST['contact']
        company = request.POST['company']
        address = request.POST['address']
        product = request.POST['material']
        official_email = request.POST['off_email']
        off_contact = request.POST['phone']
        
        
        
        getData = User.objects.filter(id=request.user.id)
        getData.update(first_name=name,
                            email=email,
                            username=username,
                            is_supplier=True,
                            # display_picture = dp,
                            # bg_picture= bg_img,
                            country = country,
                            state = state,
                            contact_no = contact,
                            company_name = company,
                            address = address,
                            Materials = product,
                            office_email = official_email,
                            off_phone_no = off_contact,
                            )
        messages.success(request, 'Profile Updated Successfull.')
        return redirect("/supplier-app/profile-edit/")
       
    else:
        getData = User.objects.get(id=request.user.id)
        return render(request, "supplier/profile-edit.html", {'getData':getData,'prod':prod,'state':state,'country':country})
    
    
def AboutCompany(request):
    if request.method == "POST":
        name = request.POST['name']
        dp = request.FILES['profile_img']
        bg_img = request.FILES['backgroud_img']
        email = request.POST['email']
        service = request.POST['service']
        discrip = request.POST['discript']
        phone = request.POST['phone']
        user = request.user.id
        obj = CompanyProfile(name=name,display_picture=dp,bg_picture=bg_img,email=email,service=service,discription=discrip,contact=phone,cretaed_by=user)
        obj.save()
        messages.success(request, "Company details create successfull.")
        return redirect('/supplier-app/company-details/')
    else:
        return render(request, 'supplier/company_profile.html')
    
    
def CompanyDetail(request):
    user = User.objects.get(id=request.user.id)
    # print(user)
    detail = CompanyProfile.objects.get(created_by_id=user)
    # print(detail)
    return render(request, "supplier/company_details.html", {'detail':detail})



def CompanyProfileEdit(request,id):
    if request.method == "POST":
        name = request.POST['name']
        dp = request.FILES.get('profile_img')
        bg_img = request.FILES.get('backgroud_img')
        email = request.POST['email']
        service = request.POST['service']
        discrip = request.POST['discript']
        phone = request.POST['phone']
        
        obj = CompanyProfile.objects.filter(id=request.user.id)
        obj.update(name=name,display_picture=dp,bg_picture=bg_img,email=email,service=service,discription=discrip,contact=phone)
        return redirect('/supplier-app/com-details/')
    else:
        obj = CompanyProfile.objects.get(id=id)
        print(obj.name)
        return render(request, "supplier/company_profile_edit.html", {'obj':obj})