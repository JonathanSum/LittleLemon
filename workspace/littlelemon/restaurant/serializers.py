#define Serializer class for User model
from rest_framework.decorators import api_view
from rest_framework import serializers, generics
from .models import MenuItem, Booking
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'inventory']
