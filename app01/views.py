from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            return Response({'message': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = User.objects.create(username=username, password=password)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username, password=password).exists():
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)