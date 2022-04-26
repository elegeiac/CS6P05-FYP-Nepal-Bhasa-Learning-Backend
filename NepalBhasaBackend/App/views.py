from django.shortcuts import render, redirect
from App.models import *
from .serializer import *
from rest_framework.settings import api_settings

from rest_framework import viewsets

    
# Create your views here.
class Phrase(viewsets.ModelViewSet):
    queryset =  Phrase.objects.all()
    serializer_class = PhraseSerializer

class Category(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class Lipi(viewsets.ModelViewSet):
    queryset = Lipi.objects.all()
    serializer_class = LipiSerializer

