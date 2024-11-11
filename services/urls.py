from django.urls import path
from . import views


app_name = 'services'
urlpatterns = [
    path('upload/', views.upload_service, name='upload_service'),
    path('display/', views.display_services, name='display_services'),
    path('services/', views.services_list, name='services_list'),
    path('request/<int:service_id>/', views.request_service, name='request_service'),
    path('requested/', views.display_requested_services, name='display_requested_services'),
]
