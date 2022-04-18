from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from posixpath import basename
from django.contrib import admin
from django.urls import path, include
from App import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from NepalBhasaBackend import settings

router = routers.DefaultRouter(trailing_slash=False)
router.register('phraseList', views.Phrase)
router.register('categoryList', views.Category)
router.register('lipiList', views.Lipi)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', obtain_auth_token, name='token'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('app/user/', include('AuthApi.urls', namespace='users')),
    path('bookmark/', include('BookmarkApi.urls', namespace='bookmarks')),
    path('feedback/', include('Feedback.urls', namespace='feedback')),
    # path(r'^static/(?P<path>.)$', serve,{'document_root': settings.STATIC_ROOT}),
    path(r'^media/(?P<path>.)$', serve,{'document_root': settings.MEDIA_ROOT}),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)