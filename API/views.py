from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from.serializers import *
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)

class SuperUserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SuperUserSerializer
    
    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password, is_staff=True, is_superuser=True)



@receiver(post_save, sender=User)
def create_userdetails(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        Userdetails.objects.create(
            national_id='00-00000A0A0',
            full_name='John Doe',
            address='123 Main St',
            phone_number='555-555-5555',
            email=instance.email,
            gender='Male'
        )


class LoginView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            print(request.data)
            return Response({'token': token.key})
        else:
            print(request.data)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return Response({'message': 'Logged out successfully'})
