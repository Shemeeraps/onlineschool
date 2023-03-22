from django.urls import path
from . import views

urlpatterns=[
    path('',views.demo,name='demo'),
    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('detail',views.detail,name='detail'),
    path('update',views.update,name='update'),
    path('updateform',views.updateform,name='updateform'),
   
]