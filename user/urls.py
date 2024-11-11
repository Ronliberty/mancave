# users/urls.py

from django.urls import path
from .views import EmployeeLoginView, ClientLoginView, ClientSignUpView, ClientLogoutView, EmployeeLogoutView, manager_profile_view, client_profile_view, manager_user_update_view, client_user_update_view, manager_password_change_view, client_password_change_view


app_name = 'user'
urlpatterns = [
    path('login/employee/', EmployeeLoginView.as_view(), name='employee_login'),
    path('logout/employee/', EmployeeLogoutView.as_view(), name='employee_logout'),
    path('login/client/', ClientLoginView.as_view(), name='client_login'),
    path('logout/client/', ClientLogoutView.as_view(), name='client_logout'),
    path('signup/client/', ClientSignUpView.as_view(), name='client_signup'),
    path('profile/manager/', manager_profile_view, name='manager_profile'),
    path('dashboard/profile/client/', client_profile_view, name='client_profile'),
    path('manager/profile/update/', manager_user_update_view, name='manager_user_update'),
    path('client/profile/update/', client_user_update_view, name='client_user_update'),
    path('manager/password/change/', manager_password_change_view, name='manager_password_change'),
    path('client/password/change/', client_password_change_view, name='client_password_change'),

]
# In urls.py


