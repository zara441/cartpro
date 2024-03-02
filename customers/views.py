from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as authlogin, logout as authlogout
from . models import Customers

# Create your views here.

def signup(request):
    if request.POST  and 'signup' in request.POST:
        try:
            username=request.POST['username']
            firstname=request.POST['fname']
            lastname=request.POST['lname']
            address=request.POST['address']
            email=request.POST['email']
            password=request.POST['password']
            phone=request.POST['phonenumber']
            print(username,password,email)

            # creating user

            user=User.objects.create_user(username=username,
                                          first_name=firstname,
                                          last_name=lastname,
                                          email=email,
                                          password=password)
            print('user created')
            
            # creating Customer account

            customer=Customers.objects.create(user=user,
                                              name=firstname,
                                              address=address,
                                              email=email,
                                              phone_number=phone)
            print('customer created')
            # return redirect('/')
            messages.success(request,'Successfully signed up')

        except Exception as e:
            error='INVALID! Invalid credentials'
            messages.error(request,error)    

    return render(request,'signup.html')

def login(request):
    if request.POST  and 'login' in request.POST:
        
        try:
            username=request.POST['username']
            password=request.POST['password']
            print(username,password)
            user=authenticate(username=username,password=password)
            if user:
                authlogin(request,user)
                print('login----------------------------->')
                return redirect('/')
            else:
                messages.info(request,'invalid credentials')
        except Exception as e:
            error='Invalid credentials'
            messages.error(request,error)

    return render(request,'login.html')

def logout(request):
    authlogout(request)
    return redirect('/')