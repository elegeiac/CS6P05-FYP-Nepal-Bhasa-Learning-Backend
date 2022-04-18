from django.urls import path
from BookmarkApi.views import BookmarkPhrase


app_name = 'BookmarkApi'
urlpatterns = [
    path('post/<str:phraseID>/', BookmarkPhrase.as_view(),name='bookmark'),
]