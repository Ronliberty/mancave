from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Index view
def indexview(request):
    return render(request, 'client/index.html')



class ClientDashboardView(View):
    def get(self, request):
        return render(request, 'client/dashboard.html')
