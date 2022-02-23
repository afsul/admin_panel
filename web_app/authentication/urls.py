from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name="home"),
   path('signup',views.signup, name="signup"),
   path('index',views.index, name="index"),
   path('signout',views.signout, name="signout"),
   path('signin',views.signin,name="signin"),
   path('adminsignin',views.adminsignin,name="adminsignin"),

]
