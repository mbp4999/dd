from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.
#taking Model view set class

class Bookviewset(viewsets.ModelViewSet):
    queryset = Booksmodel.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication]
    permissions_classes =  [IsAdminUser]