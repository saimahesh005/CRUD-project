from django.urls import path
from . import views

urlpatterns = [
    
    path('members', views.members,name='members'),
    path('home', views.home, name='home'),
    path('addrecords', views.addrecords, name= 'addrecords'),
    path('update', views.updaterecords, name='update'),
    path('delete', views.deleterecords, name='delete')
]