from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Appointment
from .forms import AppointmentForm



def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Appointment booked successfully!")
    else:
        form = AppointmentForm()
    return render(request, 'appointment/book.html', {'form': form})


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment/appointments.html', {'appointments': appointments})



