from django.shortcuts import render,redirect
from formInterface import form
from django.http import HttpResponse
from .models import UserData
from django.db import connection
# Create your views here.

def Login(request):
    if request.method == 'POST':
        loginpage= form.Loginform(request.POST)
        if(loginpage.is_valid()):
            user = loginpage.cleaned_data['Username']
            password = loginpage.cleaned_data['Password']

            db= connection.get_connection_params()['db']
            data=UserData.from_db(db,['Username','password'],values=[user,password])
            print(data)
            #redirect('signup',{'signup':form.SignUpFrom()})
    else:
        loginpage=form.Loginform()
    
    return render(request,'Html/Login.html',{'login':loginpage})


def Signup(request):
    if request.method == 'POST':
        signup = form.SignUpFrom(request.POST)

        if(signup.is_valid()):
            first = signup.cleaned_data['First_name']
            last = signup.cleaned_data['Last_name']
            password = signup.cleaned_data['Password']
            cndpswd=signup.cleaned_data['Confirm_Password']
            email = signup.cleaned_data['Email_Id']
            user = signup.cleaned_data['Username']
            terms = signup.cleaned_data['Terms_and_Conditions']

            signup.save()
            return redirect('login',{'login':form.LoginData()})
            
    else:
        signup = form.SignUpFrom()

    return render(request,'Html/Signup.html',{'signup':signup})