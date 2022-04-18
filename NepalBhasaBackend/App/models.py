
from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class Category(models.Model):
    categoryID = models.CharField(max_length=10,primary_key = True)
    categoryName = models.CharField(max_length=255)
    
    class Meta:
        db_table = "category"
        
class Phrase(models.Model):
    phraseID = models.CharField(max_length=10, primary_key = True)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    phraseMeaning = models.CharField(max_length=255)
    phraseDevnagari = models.CharField(max_length=255)
    phraseEnglish = models.CharField(max_length=255)
    phraseLipi = models.ImageField(upload_to="Lipi/", blank=True, null=True)
    phraseNarration = models.FileField(upload_to="Narration/", blank=True)
    
    class Meta:
        db_table = "phrase"



# class Favourite(models.Model):
#     email = models.ForeignKey(User, on_delete=models.CASCADE)
#     phraseID = models.ForeignKey(Phrase, on_delete=models.CASCADE)
    
#     class Meta:
#         db_table = "favourite"        

class Lipi(models.Model):
    lipiID = models.CharField(max_length=10, primary_key = True)
    lipiText = models.ImageField(upload_to="Lipi/", blank=True, null=True)
    category = models.CharField(max_length=255)
    lipiDevnagari = models.CharField(max_length=255)
    lipiEnglish = models.CharField(max_length=255)
    
    class Meta:
        db_table = "lipi"

# class Quiz(models.Model):
    
#     questionID = models.CharField(max_length=10, primary_key = True)
#     quizLevel= models.CharField(max_length=255)
#     quizCategory= models.CharField(max_length=255)
#     questionText = models.CharField(max_length=255)
#     questionAudio = models.FileField(upload_to="Narration/", blank=True, null=True)
#     questionImage = models.ImageField(upload_to="Lipi/", blank=True, null=True)
#     opt1 = models.CharField(max_length=255)
#     opt2 = models.CharField(max_length=255)
#     opt3 = models.CharField(max_length=255)
#     correctOpt = models.CharField(max_length=255)
    
#     class Meta:
#         db_table = "quiz"