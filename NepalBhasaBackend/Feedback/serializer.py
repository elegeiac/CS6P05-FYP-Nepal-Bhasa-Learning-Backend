from Feedback.models import Feedback
from rest_framework import serializers


class FeebackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'user', 'subject','description')