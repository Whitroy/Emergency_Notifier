from django.urls import path
from formInterface import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('signup',views.Signup),
    path('login',views.Login),
]