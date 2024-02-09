# urls.py
from django.urls import path

from api.views import (UserLoginAPIView,
                       UserRegistrationAPIView,
                       IhaAPIView,
                       IhaDetailAPIView,
                       KiralamaListCreateView,
                       KiralamaRetrieveUpdateDestroyView,
                       KullaniciDetayListCreateView,
                       KullaniciDetayRetrieveUpdateDestroyView)
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('api/login', UserLoginAPIView.as_view(), name='user-login'),
    path('api/register', UserRegistrationAPIView.as_view(), name='user-register'),
    path('api/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/iha', IhaAPIView.as_view(), name='iha-list-create'),
    path('api/iha/<int:pk>', IhaDetailAPIView.as_view(), name='iha-detail'),
    path('api/kiralama', KiralamaListCreateView.as_view(), name='kiralama-list-create'),
    path('api/kiralama/<int:pk>', KiralamaRetrieveUpdateDestroyView.as_view(),
         name='kiralama-retrieve-update-destroy'),
    path('api/kullanicidetay', KullaniciDetayListCreateView.as_view(), name='kullanicidetay-list-create'),
    path('api/kullanicidetay/<int:pk>', KullaniciDetayRetrieveUpdateDestroyView.as_view(),
         name='kullanicidetay-retrieve-update-destroy'),
]