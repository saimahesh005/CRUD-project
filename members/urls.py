from django.urls import path
from . import views

urlpatterns = [
    path('showrecords', views.showrecords,name='index'),
    path('members', views.members,name='members'),
    path('index2', views.index2, name='index2'),
    path('addrecords', views.addrecords, name= 'addrecords'),
    path('update', views.updaterecords, name='update'),
    path('delete', views.deleterecords, name='delete')
]