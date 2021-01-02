from django.shortcuts import render
from formInterface import form
# Create your views here.
def Login(request):
    return render(request,'Html/Login.html')

def Signup(request):
    return render(request,'Html/Signup.html')

def Loginreq(request):
    Loginformreq = form.LoginForm()

    if request.method == 'POST':
        Loginformreq = form.LoginForm(request.POST)
        html = 'we have recived this form again'
    else:
        html = 'welcome for first time'
    
    return render(request,'login.html',{'html':html,'form':form})

