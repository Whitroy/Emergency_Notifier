from django.urls import path
from formInterface import views

urlpatterns = [
    path('',views.Loginreq),
    path('signup',views.Signup)
]