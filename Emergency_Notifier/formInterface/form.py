from django import forms
from formInterface.models import UserData,LoginData

class SignUpFrom(forms.ModelForm):
    class Meta:
        model = UserData
        fields= ('First_name','Last_name','Username','Email_Id','Password','Confirm_Password','Terms_and_Conditions')
        widgets={
            'First_name': forms.TextInput(attrs={'class':'form-control'}),
            'Last_name': forms.TextInput(attrs={'class':'form-control'}),
            'Username':forms.TextInput(attrs={'class':'form-control'}),
            'Email_Id':forms.EmailInput(attrs={'class':'form-control'}),
            'Password':forms.PasswordInput(attrs={'class':'form-control'}),
            'Confirm_Password':forms.PasswordInput(attrs={'class':'form-control'}),
            'Terms_and_Conditions':forms.CheckboxInput(attrs={'class':'checkbox'})
        }

        labels={
            'First_name': 'First name',
            'Last_name': 'Last name',
            'Username':'Username',
            'Email_Id':'Email-Id',
            'Password':'Password',
            'Confirm_Password':'Confirm Password',
            'Terms_and_Conditions':'Terms and Conditions'
        }

class Loginform(forms.ModelForm):
    class Meta:
        model=LoginData
        fields='__all__'
        widgets={
            'Username':forms.TextInput(attrs={'class':'form-control'}),
            'Password':forms.PasswordInput(attrs={'class':'form-control'})
        }

