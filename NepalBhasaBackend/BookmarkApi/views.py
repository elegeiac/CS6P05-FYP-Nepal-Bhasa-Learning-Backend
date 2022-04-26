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

from BookmarkApi.serializer import BookmarkSerializer
from App.serializer import PhraseSerializer
from App.models import Phrase

# Create your views here.

# @csrf_exempt
class BookmarkPhrase(APIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = BookmarkSerializer
    # queryset = Bookmark.objects.all()
    
    def post(self, request, phraseID,format=None):
        # bookmark = Bookmark.objects.get()    
        # phrase = get_object_or_404(Phrase,id=phraseID)
       
        user_id = self.request.user.id

        print('===================')
        print(self.request.user.id)
        print('====================')

        # return HttpResponse('Found')
        if models.Bookmark.objects.filter(phrase=phraseID, user=user_id):  
            print(phraseID)
            
            models.Bookmark.objects.filter(phrase=phraseID, user=user_id).delete()
            return HttpResponse('Found')
        else:     
            data = { 'user': user_id, 'phrase': phraseID }
            serializer = BookmarkSerializer(data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return HttpResponse('NotFound')
        
    
class GetBookmarkView(generics.ListAPIView):
    serializer_class = BookmarkSerializer
    def get_queryset(self):
        user_id = self.request.user.id
        return models.Bookmark.objects.filter(user=user_id).all()