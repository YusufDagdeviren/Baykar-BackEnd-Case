# views.py
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (UserRegistrationSerializer,
                          MyTokenObtainPairSerializer,
                          IhaSerializer,
                          KiralamaSerializer,
                          KullaniciDetaySerializer)
from .models import Iha, Kiralama, KullaniciDetay

class IhaAPIView(generics.ListCreateAPIView):
    queryset = Iha.objects.all()
    serializer_class = IhaSerializer
    permission_classes = [IsAuthenticated]
class IhaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Iha.objects.all()
    serializer_class = IhaSerializer
    permission_classes = [IsAuthenticated]
class KullaniciDetayListCreateView(generics.ListCreateAPIView):
    queryset = KullaniciDetay.objects.all()
    serializer_class = KullaniciDetaySerializer
    permission_classes = [IsAuthenticated]

class KullaniciDetayRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KullaniciDetay.objects.all()
    serializer_class = KullaniciDetaySerializer
    permission_classes = [IsAuthenticated]
class KiralamaListCreateView(generics.ListCreateAPIView):
    queryset = Kiralama.objects.all()
    serializer_class = KiralamaSerializer
    permission_classes = [IsAuthenticated]

class KiralamaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kiralama.objects.all()
    serializer_class = KiralamaSerializer
    permission_classes = [IsAuthenticated]




class UserLoginAPIView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
