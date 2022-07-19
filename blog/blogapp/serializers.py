from django.urls import path, include
from .models import Category
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
    #    fields = '__all__'  # берем  все поля
        fields = ('name', 'alias')

# из статьи
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']