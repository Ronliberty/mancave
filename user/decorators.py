# decorators.py
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

def role_required(*roles):

    def in_roles(user):
        # Check if the user is authenticated and has one of the specified roles
        return user.is_authenticated and user.role in roles

    # Using user_passes_test to handle redirection if the user is not authorized
    return user_passes_test(in_roles, redirect_field_name=None, login_url='user:client_login')
