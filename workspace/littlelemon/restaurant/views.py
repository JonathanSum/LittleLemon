from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.


def sayHello(request):
 return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    ordering_fields = ['price']
    search_field = ['title']
    def get_item(self):
        return f'{self.title} : {str(self.price)}'

    # def get_permissions(self):
    #     permission_classes = []
    #     if self.request.method == 'GET':
    #         permission_classes = [IsAuthenticated]

    #     return [permission() for permission in permission_classes]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
   permission_classes = [IsAuthenticated]
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer
   permission_classes = [IsAuthenticated]