from django.urls import path
from . import views

app_name = 'appointment'
urlpatterns = [
    path('book/', views.appointment, name='book_appointment'),
    path('appointments/', views.appointment_list, name='appointment_list'),
]
