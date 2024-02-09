# serializers.py
from rest_framework import serializers
from .models import Kullanici, Iha, Kiralama, KullaniciDetay
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class IhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iha
        fields = '__all__'

class KiralamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kiralama
        fields = '__all__'
class KullaniciDetaySerializer(serializers.ModelSerializer):
    class Meta:
        model = KullaniciDetay
        fields = '__all__'

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kullanici
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}