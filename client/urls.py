from django.urls import path
from .views import indexview, ClientDashboardView

app_name = 'client'
urlpatterns = [
    path('', indexview, name='index'),
    path('dashboard/', ClientDashboardView.as_view(), name='client_dashboard'),
]
