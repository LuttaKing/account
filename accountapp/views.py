from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user_login(request):
        if request.method == 'POST':
            email=request.POST['email']
            password=request.POST['password']
           
            user = authenticate(request,username=email,password=password)
            if user is not None:
                    if user.is_active:
                        print(user.username)
                        login(request, user)
                        return HttpResponse('Authenticated successfully')
                    else:
                        return HttpResponse('Disabled account')
            else:
                    return HttpResponse('Invalid login')
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
   


