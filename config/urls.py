# urls.py
from django.urls import path

from api.views import UserLoginAPIView, UserRegistrationAPIView, IhaAPIView, IhaDetailAPIView
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('api/login', UserLoginAPIView.as_view(), name='user-login'),
    path('api/register', UserRegistrationAPIView.as_view(), name='user-register'),
    path('api/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/iha', IhaAPIView.as_view(), name='iha-list-create'),
    path('api/iha/<int:pk>', IhaDetailAPIView.as_view(), name='iha-detail')
]