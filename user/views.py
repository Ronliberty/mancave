# In views.py
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .forms import ClientRegistrationForm, ProfileUpdateForm, UserUpdateForm, CustomPasswordChangeForm
from .models import CustomUser, UserProfile



# In views.py
class EmployeeLoginView(LoginView):
    template_name = 'manager/login.html'
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)

        # Redirect based on the user's role
        if user.role == 'manager':
            return redirect('manager:dashboard')

        else:
            return redirect('user:employee_login')  # For clients


class ClientLoginView(LoginView):
    template_name = 'client/login.html'  # Separate login template for clients
    success_url = reverse_lazy('client:client_dashboard')  # URL after successful client login

    def form_valid(self, form):
        user = form.get_user()
        if user.role == 'client':
            login(self.request, user)
            return redirect(self.success_url)
        else:
            return redirect('client:index')



class ClientSignUpView(CreateView):
    model = CustomUser
    form_class = ClientRegistrationForm
    template_name = 'client/login.html'
    success_url = reverse_lazy('client:client_dashboard')  # Redirect to client dashboard after sign-up

    def form_valid(self, form):
        # Optionally, you can add any custom logic before saving the user
        return super().form_valid(form)


class ClientLogoutView(LogoutView):  # Fix indentation
    next_page = reverse_lazy('user:client_login')  # Redirect to client login page after logout


class EmployeeLogoutView(LogoutView):  # Fix indentation
    next_page = reverse_lazy('user:employee_login')



def manager_profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    form = ProfileUpdateForm(instance=user_profile)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user:manager_profile')
        else:
            form = ProfileUpdateForm(instance=user_profile)


    return render(request, 'user/manager_profile.html', {'form': form})

@login_required
@role_required('client')
def client_profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)


    form = ProfileUpdateForm(instance=user_profile)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user:client_profile')


    return render(request, 'user/client_profile.html', {'form': form})


@login_required
@role_required('manager')
def manager_user_update_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('user:manager_user_update')
    else:
        form = UserUpdateForm(instance=request.user)  # This line handles GET requests

    return render(request, 'user/manager_update.html', {'form': form})


def client_user_update_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('user:client_user_update')
    else:
        form = UserUpdateForm(instance=request.user)  # This line handles GET requests

    return render(request, 'user/client_update.html', {'form': form})

@login_required
@role_required('manager')
def manager_password_change_view(request):
    if request.method == 'POST':
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            password_form.save()
            messages.success(request, 'Your password has been changed successfully!')
            return redirect('user:employee_login')  # Redirect to the login page or another page
    else:
        password_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'user/manager_password.html', {'password_form': password_form})


@login_required
@role_required('client')
def client_password_change_view(request):
    if request.method == 'POST':
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            password_form.save()
            messages.success(request, 'Your password has been changed successfully!')
            return redirect('user:client_login')  # Redirect to the login page or another page
    else:
        password_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'user/client_password.html', {'password_form': password_form})
