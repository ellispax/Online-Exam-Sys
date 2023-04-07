from rest_framework import generics, permissions
from .models import UserDetails, Question, AnswerOption, ExamAttempt, UserAnswer
from .serializers import UserDetailsSerializer, QuestionSerializer, AnswerOptionSerializer, ExamAttemptSerializer, UserAnswerSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserDetailsSerializer
from django.shortcuts import render, redirect
from django.contrib import messages, auth

from django.contrib.auth.models import User
from django.http import JsonResponse



class UserList(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer
    #permission_classes = [permissions.IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

class AnswerOptionList(generics.ListCreateAPIView):
    queryset = AnswerOption.objects.all()
    serializer_class = AnswerOptionSerializer
    permission_classes = [permissions.IsAuthenticated]

class AnswerOptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnswerOption.objects.all()
    serializer_class = AnswerOptionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExamAttemptList(generics.ListCreateAPIView):
    queryset = ExamAttempt.objects.all()
    serializer_class = ExamAttemptSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExamAttemptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamAttempt.objects.all()
    serializer_class = ExamAttemptSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserAnswerList(generics.ListCreateAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserAnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserCreateAPIView(APIView):
    """
    View to create a new user instance.
    """
    def post(self, request):
        serializer = UserDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)



def register(request):
    if request.user.is_authenticated:
        return JsonResponse({'error': 'User is already authenticated'})

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'That username is taken'})
            else:
                if User.objects.filter(email=email).exists():
                    return JsonResponse({'error': 'That email is being used'})
                else:
                    user = User.objects.create_user(
                        username=username, password=password, 
                        email=email, first_name=first_name, last_name=last_name
                    )
                    user.save()
                    return JsonResponse({'success': 'Your account has been created! You can now login.'})
        else:
            return JsonResponse({'error': 'Passwords do not match'})
    else:
        return JsonResponse({'error': 'POST request is required'})
