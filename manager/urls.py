from django.urls import path
from .views import dashboard

app_name = 'manager'
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
]
