from pyexpat import model
from django.contrib import admin

from BookmarkApi import models

# Register your models here.
@admin.register(models.Bookmark)
class BookmarkApiAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phrase')