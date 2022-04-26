
from django.db import models
from django.contrib.auth.models import User, AbstractUser


#Database Model for Category
class Category(models.Model):
    categoryID = models.CharField(max_length=10,primary_key = True)
    categoryName = models.CharField(max_length=255)
    
    class Meta:
        db_table = "category"


#Database Model for Phrase        
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
    
#Database Model for Lipi
class Lipi(models.Model):
    lipiID = models.CharField(max_length=10, primary_key = True)
    lipiText = models.ImageField(upload_to="Lipi/", blank=True, null=True)
    category = models.CharField(max_length=255)
    lipiDevnagari = models.CharField(max_length=255)
    lipiEnglish = models.CharField(max_length=255)
    
    class Meta:
        db_table = "lipi"

