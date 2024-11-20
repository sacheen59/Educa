from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def user_registration(request):
    """
    function to register the user
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Account created Successfully')
            return redirect('login')
        else:
            messages.add_message(request,messages.ERROR,'Failed to create an account')
            return render(request, 'accounts/register.html',{
                'form':form
            })
    return render(request,'accounts/register.html',{
        'form':UserCreationForm
    })

def user_login(request):
    """
    function to login user
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username = cd['username'],password = cd['password'])
            if user is not None:
                login(request,user)
                return redirect('manage_course_list')
            else:
                messages.add_message(request,messages.ERROR,'Please provide correct credentials')
                return render(request,'accounts/user_login.html',{'form':form})
    return render(request, 'accounts/user_login.html',{
        'form':LoginForm
    })


def user_logout(request):
    logout(request)
    return redirect('login')

