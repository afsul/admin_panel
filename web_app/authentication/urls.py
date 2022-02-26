from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include, re_path

urlpatterns = [
   path('',views.home,name="home"),
   path('signup',views.signup, name="signup"),
   path('index',views.index, name="index"),
   path('signout',views.signout, name="signout"),
   path('signin',views.signin,name="signin"),
   path('adminsignin',views.adminsignin,name="adminsignin"),
   path('edit/<int:id>',views.edit,name="edit"),
   path('update/<int:id>',views.update,name="update"),
   path('delete/<int:pk>', views.delete, name="delete"),
   path('search',views.search_list,name="search"),
   path('adminlogout',views.adminlogout,name="adminlogout"),


]  
