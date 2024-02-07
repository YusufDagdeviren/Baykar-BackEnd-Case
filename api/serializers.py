# serializers.py
from rest_framework import serializers
from .models import Kullanici

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kullanici
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}