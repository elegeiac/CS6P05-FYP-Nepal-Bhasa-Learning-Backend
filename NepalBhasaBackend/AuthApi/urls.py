from django.urls import include, path

from AuthApi.views import CustomUserCreate


app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    # path('get_current_user/', GetCurrentUser.as_view(), name="current_user"),
]

