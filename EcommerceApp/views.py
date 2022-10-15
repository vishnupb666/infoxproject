import math
import random
from django.shortcuts import render
import os
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    cate = category.objects.all()
    return render(request,'home.html',{'cate':cate})

def generateOTP() :
 
    # Declare a digits variable 
    # which stores all digits
    digits = "0123456789"
    OTP = ""
 
   # length of password can be changed
   # by changing value in range
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP

def sign_up(request):
    
    if request.method=='POST':
        
        fname = request.POST['fname']
        username = request.POST['username']
        lname = request.POST['lname']
        address = request.POST['address']
        phone = request.POST['phone']
        gender = request.POST['gender']
        state = request.POST['state']
        district = request.POST['district']
        dob = request.POST['dob']
        pincode = request.POST['pincode']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']
        pro = request.FILES.get('pro_pic')
        if pro is not None:
            pro_pic = pro
        else:
            pro_pic ='static/image/user.jpg'
        try:    
            if password==c_password:
                if User.objects.filter(username = username).exists():
                    messages.info(request,'this user name is already exist')
                    return redirect('sign_up')
                else:
                    user = User.objects.create_user(
                        first_name=fname,
                        last_name = lname,
                        username = username,
                        password=password,
                        email=email,
                    )
                    
                    e_user = user_ext(
                        user_id= User.objects.get(id=user.id),
                        date_of_birth = dob,
                        image=pro_pic,
                        gender=gender,
                        phone=phone,
                        address=address,
                        state=state,
                        district=district,
                        otp= generateOTP(),
                        pincode = pincode,
                    )
        except:
            messages.info('username or password incorrect...')
            return redirect('sign_up')
        else:
            user.save()
            e_user.save()
            messages.info(request,f'{username} success fully created account ')
            return redirect('sign_up')
    return render(request,'sign_up.html')
    

def log_in(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
    return render(request,'log_in.html')

@login_required(login_url='log_in')
def log_out(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url='log_in')
def viewprofile(request):
    user = request.user
    pro_detail = User.objects.get(id=user.id)
    return render(request,'profile/profile.html',{'data':pro_detail})
@login_required(login_url='log_in')
def updateprofile(request):
    user = request.user
    update = User.objects.get(id=user.id)
    if request.method=="POST":
        update.first_name = request.POST['fname']
        update.username = request.POST['username']
        update.last_name = request.POST['lname']
        update.user_ext.address = request.POST['address']
        update.user_ext.user_phone = request.POST['phone']
        update.user_ext.gender = request.POST['gender']
        update.user_ext.state = request.POST['state']
        update.user_ext.district = request.POST['district']
        update.user_ext.state = request.POST['state']
        update.user_ext.dob = request.POST['dob']
        update.pincode = request.POST['pincode']
        update.user_ext.email = request.POST['email']
        update.password = request.POST['password']
        pro = request.FILES.get('pro_pic')
        if pro is not None:
            if pro != request.POST.get('edit_pic'):
                if request.POST.get('edit_pic')!='static/image/user.jpg':
                    os.remove(update.user_ext.image.path) 
            update.user_ext.pro_pic = pro
        else:
            update.user_ext.pro_pic = request.POST.get('edit_pic') 

        if update.password == request.POST['password']:
            messages.info(request,'password was incorrect')
        else:
            update.save()
            return render('viewprofile')
@csrf_exempt
def addcategory(request):
    if request.user.is_superuser:
        if request.method=="POST":
            name = request.POST.get('category')
            image = request.FILES.get('image')
            
            cat_item = category(name=name,image=image)
            cat_item.save()
            return JsonResponse({'status':1})
        else:
            pass

        return render(request,'admin/addcategory.html')
    return render(request,'admin/addcategory.html')
def listCategory(request):
    x = category.objects.all()
    return render(request,'admin/listcatgory.html',{'data':x})


def admin_dash(request):
    cate = category.objects.all()
    return render(request,'admin/admindash.html',{'cate':cate})

@csrf_exempt
def addproduct(request):
    cate_gory = category.objects.all()
    if request.user.is_superuser:
        if request.method=="POST":
            name = request.POST.get('product')
            amount = request.POST.get('amount')
            cate_id = request.POST.get('category')
            
            image = request.FILES.get('image')
            cate = category.objects.get(id=cate_id)
            pro_item = product(name=name,category_id=cate,image=image,amount=amount)
            pro_item.save()
            return JsonResponse({'status':1})
        else:
            pass

        return render(request,'admin/addproduct.html',{'cat':cate_gory})
    else:
        pass
    

    return render(request,'admin/addproduct.html',{'cat':cate_gory})

def listProduct(request,):
    x = product.objects.all()
    return render(request,'admin/listproduct.html',{'data':x})

def view_users(request):
    users = User.objects.all()
    return render(request,'admin/viewusers.html',{'users':users})
         
def searchProd(request,pk):
    prod = product.objects.filter(category_id=pk)
    return render(request,'users/user_prolist.html',{'data':prod})

def addkartView(request,pk):
    user=request.user
    pro = product.objects.get(id = pk)
    id = User.objects.get(id= user.id)
    kart_item=kart(user_id = id,product_id=pro)
    kart_item.save()
    return JsonResponse({'status':1})

def viewKart(request,pk):
    cate = category.objects.all()
    user_data = kart.objects.filter(user_id = pk)
    return render(request,'kart_view.html',{'kart_detail':user_data,'cate':cate})

    
    


