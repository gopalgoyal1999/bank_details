from django.urls import path
from . import views

urlpatterns = [
path('',views.Bankdetails.as_view(),name='bankdetails'),
path('banklist/',views.Banklistdetails.as_view(),name='banklist'),
]