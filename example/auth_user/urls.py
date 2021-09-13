from django.urls import path
from .views import *

urlpatterns = [
    path('login', login_view, name='login_view'),
    path('login_process', login_request, name='login_request'),
    path('register', register_view, name='register_view'),
    path('registered', register, name='register'),
    path('logout', logout_user, name='logout'),
]
