from django.urls import path
from formInterface import views

urlpatterns = [
    path('signup',views.Signup),
    path('login',views.Login)
]