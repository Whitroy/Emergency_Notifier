from django.db import models

# Create your models here.
class UserData(models.Model):
    First_name = models.CharField(max_length = 20,default="")
    Last_name = models.CharField(max_length = 20,default="" )
    Username = models.CharField(max_length=50,primary_key=True,default="")
    Email_Id = models.EmailField(default="")
    Password = models.CharField(max_length=40,default="")
    Confirm_Password = models.CharField(max_length=40,default="")
    Terms_and_Conditions=models.BooleanField(default=False)
    City = models.CharField(max_length=20,default="")
    State = models.CharField(max_length=20,default="")
    Country = models.CharField(max_length=20,default="")
    Longitude = models.FloatField(verbose_name="Longitude of Current Location",default=0.0)
    Latitude = models.FloatField(verbose_name="Latitude of Current Location",default=0.0)

    class meta:
        db_table = 'User Data'

    def __str__(self):
        return self.First_name+" "+self.last_name

class LoginData(models.Model):
    Username = models.CharField(max_length=50,default="")
    Password = models.CharField(max_length=40,default="")

    class meta:
        db_table = 'Login Data'
    
    def __str__(self):
        return self.Username