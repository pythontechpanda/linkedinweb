from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from Supplier.models import *
from django.contrib import messages

@login_required
def demo(request):
    sup_count = User.objects.filter(is_supplier=1).count()
    by_count = User.objects.filter(is_staff=1).count()
    print(sup_count)
    return render(request, "admin/dashboard.html", {'sup_count':sup_count,'by_count':by_count})


def add_country(request):
    # num_of_sup = User.objects.filter(is_supplier = 1).count()
    # a = User.objects.all()
    # print(a)
    data = Country.objects.all()
    if request.method == "POST":
        country = request.POST['name']
        
        if Country.objects.filter(country = country).first():
            messages.success(request, 'Country name is taken.')
            return redirect('/admin-app/country/')
        
        con_obj = Country(country=country)
        con_obj.save()
        messages.success(request, 'Country Added Successfull.')
    return render(request, "admin/country.html", {'data':data})



def add_state(request):
    data = Country.objects.all()
    show_st = State.objects.all()
    print(data)
    if request.method == "POST":
        state = request.POST['name']
        country = request.POST['country_id']
        
        
        if State.objects.filter(state = state).first():
            messages.success(request, 'State name is taken.')
            return redirect('/admin-app/state/')
        
        con_obj = State(state=state, con_id_id = country)
        con_obj.save()
        messages.success(request, 'State Added Successfull.')
    return render(request, "admin/state.html", {'data':data, 'show_st':show_st})



def add_city(request):
    data = State.objects.all()
    show_ct = City.objects.all()
    print(show_ct)
    for i in show_ct:
        print(i.city, i.state)
    if request.method == "POST":
        city = request.POST['name']
        state = request.POST['state_id']
        
        if City.objects.filter(city = city).first():
            messages.success(request, 'City name is taken.')
            return redirect('/admin-app/city/')
        
        con_obj = City(city=city, state_id=state)
        con_obj.save()
        messages.success(request, 'City Added Successfull.')
    return render(request, "admin/city.html", {'data':data, 'show_ct':show_ct})


def User_list(request):
    user = User.objects.all()
    return render(request, "admin/users.html", {'user':user})


def MaterialOption(request):
    data = MaterialOptions.objects.all()

    if request.method == "POST":
        opt = request.POST['name']
        
        if MaterialOptions.objects.filter(opetion = opt).first():
            messages.success(request, 'Option already taken.')
            return redirect('/admin-app/material/')
        
        con_obj = MaterialOptions(opetion=opt)
        con_obj.save()
        messages.success(request, 'Option Added Successfull.')
    return render(request, "admin/materials.html", {'data':data})


def BuyOption(request):
    data = BuyingOption.objects.all()

    if request.method == "POST":
        opt = request.POST['name']
        
        if BuyingOption.objects.filter(opetion = opt).first():
            messages.success(request, 'Buying Option already taken.')
            return redirect('/admin-app/buying/')
        
        con_obj = BuyingOption(opetion=opt)
        con_obj.save()
        messages.success(request, 'Buying Option Added Successfull.')
    return render(request, "admin/buy_option.html", {'data':data})



def LookingOption(request):
    print("welcome")
    data = LookingFor.objects.all()
    
    print(data)

    if request.method == "POST":
        opt = request.POST['name']
        
        if LookingFor.objects.filter(opetion = opt).first():
            messages.success(request, 'Looking For already taken.')
            return redirect('/admin-app/looking/')
        
        con_obj = LookingFor(opetion=opt)
        con_obj.save()
        messages.success(request, 'Looking For Added Successfull.')
    return render(request, "admin/looking.html", {'data':data})