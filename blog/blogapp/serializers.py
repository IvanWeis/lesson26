# из статьи
from rest_framework import serializers
from django.contrib.auth.models import User

#  User:
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

# Tovar
from .models import Tovar

class TovarSerializer(serializers.ModelSerializer):
#    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Tovar
        fields = ['id', 'name', 'price']
