from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('recharge/', views.recharge, name='recharge'),
    path('login2/', views.login2, name='login2'),
    path('information/', views.information, name='information'),
    path('logout/', views.logout, name='logout'),
    path('pwd/', views.pwd, name='pwd'),
    path('ip1/', views.ip1, name='ip1'),

]
