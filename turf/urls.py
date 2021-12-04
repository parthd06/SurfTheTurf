from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book_now", views.book_now, name="book_now"),
    path("turf_details", views.turf_details, name="turf_details"),
    path("slot_details", views.slot_details, name="slot_details"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout, name="logout"),
    path("contactus", views.contactus, name="contactus"),
    path("aboutus", views.aboutus, name="aboutus"),
    path('turfBilling', views.turfBilling, name='turfBilling'),
    path('orderHistory', views.orderHistory, name="orderHistory"),
    path('allBookings', views.allBookings, name="allBookings"),
    path('delete_booking/<int:id>', views.delete_booking, name="delete_booking"),
    path('success', views.success, name='success')
]