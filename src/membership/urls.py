from django.contrib import admin
from django.urls import path 

from .views import * 






urlpatterns = [
    
    #Auth
    
    path('signup/', signupuser, name="signupuser"),
    path('logout/', logoutuser, name="logoutuser"),
    path('login/', loginuser, name="loginuser"),
    
]
