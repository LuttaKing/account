from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Post,Account

@csrf_exempt
def user_login(request):
        if request.method == 'POST':
            email=request.POST['email']
            password=request.POST['password']
           
            user = authenticate(request,username=email,password=password)
            if user is not None:
                    if user.is_active:
                        #login(request, user)
                        return HttpResponse(user.username+' Authenticated successfully')
                    else:
                        return HttpResponse('Disabled account')
            else:
                    return HttpResponse('Invalid Login Credentials')
        else:
            return HttpResponse('Post req only')
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password1']
       # password2=request.POST['password2']

        user = User.objects.create_user(username, email, password)
   
        return HttpResponse('REgistered Successfully')

@csrf_exempt
def create_user_acc(request):
    if request.method == 'POST':
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        
        try:
           userAcc = Account.objects.create_user(email,username,password)
        except :
            print('Error registering user')
   
        return HttpResponse('REgistered Successfully')


@csrf_exempt
def updateAccInfo(request):
    if request.method == 'POST':
        curr_username=request.POST['curr_username']
        new_username=request.POST['new_username']
        
        userAcc = Account.objects.filter(username=curr_username)
        Account.set_password(userAcc,raw_password=new_username)
       
       
     #   userAcc.update(username=new_username)
        

        return HttpResponse('name changed successfully')
       
   
        
   


