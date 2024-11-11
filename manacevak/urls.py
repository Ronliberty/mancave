
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('client.urls')),
    path('manager/', include('manager.urls')),
    path('appointment/', include('appointment.urls')),
    path('user/', include('user.urls')),
    path('services/', include('services.urls')),
    path('chart/', include('chart.urls')),

]
