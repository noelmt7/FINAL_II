from django.urls import path
from . import views

urlpatterns = [
    path('', views.Booking, name='Booking'),  # This is the root URL pattern
    path('Booking/', views.Booking, name='Booking'),
]
