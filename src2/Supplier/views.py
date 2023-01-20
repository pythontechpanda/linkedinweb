from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from Supplier.models import CoursesOptions, Country,State,City
from django.contrib import messages
from Supplier.models import *
from datetime import datetime
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
import geocoder
import folium
from geopy.geocoders import Nominatim

def demo(request):
    getData = User.objects.get(id=request.user.id)
    all_post = CreatePost.objects.filter(author=getData).order_by("id").reverse()
    return render(request, "supplier/index.html", {'mypost':all_post})



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
    
    
# Working on Posts

def PostCreate(request):
    if request.method == "POST":
        discription = request.POST['discrip']
        post = request.FILES['image']
        created_by = request.user.id
        post_date = datetime.now()
        
        create = CreatePost(discription=discription, post_img=post,author_id=created_by,date=post_date)
        create.save()
        messages.success(request, "Post created successfull.")
        return redirect('/supplier-app/')
    else:
        getUser = User.objects.get(id=request.user.id)
        showPost = CreatePost.objects.filter(author=getUser)   
        return render(request, "supplier/post_create.html", {'mypost':showPost})
    
    
    
def LikeView(request):
    user = request.user
    if request.method =="POST":
        post_id = request.POST.get('post_id')
        post_obj = CreatePost.objects.get(id=post_id)
        
        if user in post_obj.like.all():
            post_obj.like.remove(user)
        else:
            post_obj.like.add(user)
        
        like, created =LikePost.Objects.get_or_create(user=user, post_id=post_id)
        
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
                
        like.save()
    return redirect('/supplier-app/')
    # return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found')) 




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

    return redirect('/supplier-app/')

  
def post_comment_create_and_list_view(request):
    qs = CreatePost.objects.all()
    profile = User.objects.get(user=request.user)
    
    
    if 'submit_c_form' in request.POST:
        c_form = CommentModelForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id=request.POST.get('post_id'))
            instance.save()