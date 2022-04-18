from django.conf import settings
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL

class Feedback(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
    subject = models.TextField(max_length=255)
    description = models.TextField(max_length= 500)
    
    objects = models.Manager()