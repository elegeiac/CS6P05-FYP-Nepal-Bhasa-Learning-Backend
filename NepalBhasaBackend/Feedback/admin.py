from pyexpat import model
from django.contrib import admin

from Feedback import models

# Register your models here.
@admin.register(models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'description')