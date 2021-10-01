from django.urls import path
from . import views

urlpatterns = [
    path('', views.getjsonfile) #default function
    path('getjsonfile', views.getjsonfile)
    path('storejsonfile', views.storejsonfile)
]
