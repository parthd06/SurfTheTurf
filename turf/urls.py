from django.urls import path, include
from . import views
# from django_email_verification import urls as email_urls

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
    # path('about', views.about, name="about"),
    # path('services', views.services, name="services"),
    # path('contact', views.contact, name="contact"),
    # path('destination_details/<int:id>', views.destination_details, name='destination_details'),
    # path('booking/<int:id>', views.booking, name="booking"),
    # path('receipt', views.receipt, name='receipt'),
    # path('search', views.search, name='search'),
    # path('turfDateSelection', views.turfDateSelection, name="turfDateSelection"),
    # path('turfBookings', views.turfBookings, name="turf_bookings"),
    path('turfBilling', views.turfBilling, name='turfBilling'),
    # path('confirm_booking', views.confirm_booking, name='confirm_booking'),
    path('orderHistory', views.orderHistory, name="orderHistory"),
    path('allBookings', views.allBookings, name="allBookings"),
    # path('searchBooking', views.searchBooking, name="searchBooking"),
    path('Booked', views.Booked, name="Booked"),
    # path('email/', include(email_urls)),
    path('delete_booking/<int:id>', views.delete_booking, name="delete_booking"),
    # path('sortBy', views.sortBy, name="sortBy"),
]