from urllib import request
from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework import generics
from BookmarkApi import models
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from rest_framework.generics import GenericAPIView

from Feedback.serializer import FeebackSerializer

# Create your views here.

# @csrf_exempt
class FeedbackView(APIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = FeebackSerializer
    # queryset = Bookmark.objects.all()
    
    def post(self, request, format=None):

       
        user_id = self.request.user.id

        print('===================')
        print(request.data)
        print('====================')
            
        data = { 'user': user_id, 'subject': request.data['subject'], 'description': request.data['description'] }
        serializer = FeebackSerializer(data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse('NotFound')
      
        
