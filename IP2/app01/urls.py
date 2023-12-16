from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    # path('zc/', views.zc, name='zc'),
    path('index/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('create/', views.create, name='create'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('ip1/', views.ip1, name='ip1'),
    path('carmy/', views.carmy, name='carmy'),
]
