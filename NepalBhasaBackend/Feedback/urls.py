from django.urls import path
from Feedback.views import FeedbackView


app_name = 'Feedback'
urlpatterns = [
    path('post/', FeedbackView.as_view(),name='feedback'),
]