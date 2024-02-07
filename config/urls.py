# urls.py
from django.urls import path

from api.views import UserLoginAPIView, UserRegistrationAPIView


urlpatterns = [
    path('api/login', UserLoginAPIView.as_view(), name='user-login'),
    path('api/register', UserRegistrationAPIView.as_view(), name='user-register'),
]