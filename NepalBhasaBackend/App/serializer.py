from unicodedata import category
from rest_framework import serializers
from .models import *

class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = [
        'phraseID',
        'categoryID',
        'phraseMeaning',
        'phraseDevnagari',
        'phraseEnglish',
        'phraseLipi',
        'phraseNarration',
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
        'categoryID',
        'categoryName'
        ]

class LipiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lipi
        fields = [
        'lipiID',
        'lipiText',
        'category',
        'lipiDevnagari',
        'lipiEnglish'
        ]

# class QuizSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Quiz
#         fields = [
#         'questionID',
#         'quizLevel',
#         'quizCategory',
#         'questionText',
#         'questionAudio',
#         'questionImage',
#         'opt1',
#         'opt2',
#         'opt3',
#         'correctOpt'
#         ]
   
