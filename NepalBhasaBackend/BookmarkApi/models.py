from django.conf import settings
from django.db import models

from App.models import Phrase
# Create your models here.
User = settings.AUTH_USER_MODEL

class Bookmark(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
    phrase = models.ForeignKey(Phrase, default=1, null=True, on_delete=models.CASCADE)
    
    objects = models.Manager()