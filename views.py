from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('user1')
        uname=request.POST.get('user2')
        email=request.POST.get('email')
        pnumber=request.POST.get('phone')
        pass1=request.POST.get('lock-alt1')
        pass2=request.POST.get('lock-alt2')

        

        if pass1!=pass2:
            return HttpResponse("Oops!!! Incorrect Password/Username ¯\_(ツ)_/¯")
        else: 
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    
    return render(request,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("(-_-)zzz !!! incorrect password")
        
    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def style(request):
    return render(request,'signup.html')

#create your views here
