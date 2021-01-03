from django.shortcuts import render,redirect
from formInterface import form
from django.http import HttpResponse
# Create your views here.

def Login(request):
    return HttpResponse('<h1> submitted</h1>')

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
            return redirect('/login')
            
    else:
        signup = form.SignUpFrom()

    return render(request,'Html/Signup.html',{'signup':signup})