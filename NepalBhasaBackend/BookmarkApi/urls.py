from django.urls import path
from BookmarkApi.views import BookmarkPhrase
from BookmarkApi.views import GetBookmarkView


app_name = 'BookmarkApi'
urlpatterns = [
    path('post/<str:phraseID>/', BookmarkPhrase.as_view(),name='bookmark'),
     path('get/', GetBookmarkView.as_view(),name='getBookmark'),
    
]